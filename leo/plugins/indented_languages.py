#@+leo-ver=5-thin
#@+node:ekr.20230917013414.1: * @file ../plugins/indented_languages.py
#@+<< docstring: indented_languages.py >>
#@+node:ekr.20231023052313.1: ** << docstring: indented_languages.py >>
"""
A plugin that creates **study outlines** in which indentation replaces curly brackets.

This plugin is surprisingly helpful in getting the feel of source code.

Warnings:

- For C and Typescript, this plugin assumes that indentation corresponds to curly-bracket level!
- If this assumption is violated the results may be misleading.
- Do *not* assume that it is possible to recreate curly-brackes from the indented code!

Hacks for increased readablily:
    
- Remove the first block comment (a copyright message) in each file.
- Remove #include statements.
- Replace multiple blank lines by a single blank line.

Won't do:
    
1. This plugin could generate leading whitespace (lws) corresponding to
   curly-bracket level. Doing so would be tricky because the plugin should
   preserve lws inside parens and square brackets.

2. This plugin could support options for disabling the hacks listed above.
  
"""
#@-<< docstring: indented_languages.py >>

import re
from typing import Any, Callable, Optional
from leo.core import leoGlobals as g
from leo.core.leoNodes import Position
from leo.plugins.importers.c import C_Importer
from leo.plugins.importers.typescript import TS_Importer

#@+others
#@+node:ekr.20230917084259.1: ** top-level
#@+node:ekr.20230917015308.1: *3* init (indented_languages.py)
def init() -> bool:
    """Return True if the plugin has loaded successfully."""
    # g.registerHandler('after-create-leo-frame', onCreate)
    # g.registerHandler('after-reading-external-file', onAfterRead)
    # g.registerHandler('before-writing-external-file', onBeforeWrite)
    return True
#@+node:ekr.20231022071443.1: *3* commands (indented_languages.py)
@g.command('import-to-indented-c')
def import_to_indented_c(event: Any) -> None:
    """The import-to-indented-c command."""
    c = event.get('c')
    if c:
        Indented_C(c).do_import()

@g.command('import-to-indented-lisp')
def import_to_indented_elisp(event: Any) -> None:
    """The import-to-indented-lisp command."""
    c = event.get('c')
    if c:
        Indented_Lisp(c).do_import()

@g.command('import-to-indented-typescript')
def import_to_indented_typescript(event: Any) -> None:
    """The import-to-indented-typescript command."""
    c = event.get('c')
    if c:
        Indented_TypeScript(c).do_import()


#@+node:ekr.20231022073438.1: **  class Indented_Importer
class Indented_Importer:
    """The base class for all indented importers."""

    extensions: list[str] = None  # The file extension for the language.
    language: str = None  # The name of the language.
    importer_class: Callable = None  # The importer class

    def __init__(self, c):
        self.c = c
        self.file_name = None  # Set by import_one_file.
        if self.importer_class:
            self.importer = self.importer_class(c)  # pylint: disable=not-callable

    #@+others
    #@+node:ekr.20231022073537.1: *3* indented_i.do_import (driver)
    def do_import(self) -> Optional[Position]:
        """
        Base_Indented_Importer.do_import: Create a top-level node containing study outlines for all files in
        c.p and its descendants.

        Return the top-level node for unit tests.
        """
        c, p, u = self.c, self.c.p, self.c.undoer

        assert self.extensions

        def predicate(p: Position) -> bool:
            return self.isAtFileNode(p) and p.h.strip().endswith(tuple(self.extensions))

        roots: list[Position] = g.findRootsWithPredicate(c, p, predicate)  # Removes duplicates
        if not roots:
            return None

        # Undoably create top-level organizer node and import all files.
        try:
            ### g.app.disable_redraw = True
            last = c.lastTopLevel()
            c.selectPosition(last)
            undoData = u.beforeInsertNode(last)
            # Always create a new last top-level node.
            parent = last.insertAfter()
            parent.v.h = 'indented files'
            for root in roots:
                self.import_one_file(root, parent)
            u.afterInsertNode(parent, 'recursive-import', undoData)
        except Exception:
            g.es_print(f"Exception in {self.__class__.__name__}")
            g.es_exception()
        finally:
            ### g.app.disable_redraw = False
            for p2 in parent.self_and_subtree(copy=False):
                p2.contract()
            c.redraw(parent)
        return parent
    #@+node:ekr.20231022100000.1: *3* indented_i.import_one_file
    def import_one_file(self, p: Position, parent: Position) -> None:
        """
        Indented_Importer.import_one_file: common setup code.

        p is an @<file> node.

        - Create a parallel tree as the last child of parent.
        - Indent all the nodes of the parallel tree.
        """
        self.file_name = self.atFileName(p)

        # Create root, a parallel outline.
        root = p.copyWithNewVnodes()
        n = parent.numberOfChildren()
        root._linkAsNthChild(parent, n)
        root.h = self.file_name

        # Indent the parallel outline.
        self.indent_outline(root)

    #@+node:ekr.20231022073306.3: *3* indented_i.indent_outline (the pipeline)
    def indent_outline(self, root: Position) -> None:
        """
        Indent the body text of root and all its descendants.
        """
        for p in root.self_and_subtree():
            self.indent_node(p)
            self.remove_trailing_semicolons(p)
            self.remove_includes(p)
            self.remove_blank_lines(p)

        # Remove @path.
        if root.b.startswith('@path'):
            lines = g.splitLines(root.b)
            root.b = ''.join(lines[1:])

        # Remove the useless first block comment.
        self.remove_first_block_comment(root)

        # Append @language.
        if '@language' not in root.b:
            root.b = root.b.rstrip() + f"\n\n@language {self.language}\n"
    #@+node:ekr.20231022073306.6: *4* indented_i.indent_node
    curlies_pat = re.compile(r'{|}')
    close_curly_pat = re.compile(r'}')
    semicolon_pat = re.compile(r'}\s*;')

    def indent_node(self, p: Position) -> None:
        """
        Remove curly brackets from p.b.

        Do not remove matching brackets if ';' follows the closing bracket.
        """

        tag=f"{g.my_name()}"
        if not p.b.strip():
            return

        def oops(message):
            g.es_print(f"{self.file_name:>30}: {message}")

        lines = g.splitLines(p.b)
        guide_lines = self.importer.make_guide_lines(lines)

        # The stack contains tuples(curly_bracket, line_number, column_number) for each curly bracket.
        # Note: adding a 'level' entry to these tuples would be tricky.
        stack: list[tuple[str, int, int]] = []
        info: dict[tuple, tuple] = {}  # Keys and values are tuples, as above.

        # Pass 1: Create the info dict.
        level = 0  # To check for unmatched braces.
        for line_number, line in enumerate(guide_lines):
            last_column = 0
            for m in re.finditer(self.curlies_pat, line):
                curly = m.group(0)
                column_number = m.start()
                assert last_column == 0 or last_column < column_number, f"{tag} unexpected column"
                assert 0 <= column_number < len(line), f"{tag} column out of range"
                last_column = column_number
                # g.trace(f" {curly} lvl: {level} col: {column_number:3} line: {line_number:3} {line!r}")
                if curly == '{':
                    stack.append((curly, line_number, column_number))
                else:
                    assert curly == '}', f"{tag}: not }}"
                    if not stack:
                        oops(f"   Stack underflow: {p.h}")
                        return
                    top = stack.pop()
                    top_curly, top_line_number, top_column_number = top
                    assert top_curly == '{', f"{tag} stack mismatch"
                    this_info = (curly, line_number, column_number)
                    info [top] = this_info
                    info [this_info] = top
                level += (1 if curly == '{' else -1)
        if level != 0:
            oops(f"Unmatched brackets: {p.h} level: {level}")
            return

        # Pass 2: Make the substitutions when '}' is seen.
        result_lines = []  # Must be empty here.
        for line_number, line in enumerate(guide_lines):

            if '}' not in line:
                # No substitution is possible.
                result_lines.append(lines[line_number])
                continue

            # Typescript only: Don't make the substitution if '};' appears on the line.
            if self.language == 'typescript' and self.semicolon_pat.search(line):
                # g.trace('Skip };', repr(line))
                result_lines.append(lines[line_number])
                continue

            for m in re.finditer(self.close_curly_pat, line):
                column_number = m.start()
                this_info = ('}', line_number, column_number)
                assert this_info in info, f"no matching info: {this_info}"
                match_curly, match_line, match_column = info [this_info]
                assert match_curly == '{', f"{tag}: wrong matching curly bracket"

                # Don't make the substitution if the match is on the same line.
                if match_line == line_number:
                    # g.trace('Same line', repr(line))
                    result_lines.append(lines[line_number])
                    break

                if 0:
                    print('')
                    print(f"{tag} Remove")
                    print(f"matching: {{ line: {match_line:3} column: {match_column:2} {guide_lines[match_line]!r}")
                    print(f"    this: }} line: {line_number:3} column: {column_number:2} {line!r}")

                # Replace the previous line in result_lines, *not* lines.
                s = result_lines[match_line]
                new_line = s[:match_column] + ' ' + s[match_column + 1:]
                result_lines[match_line] = new_line.rstrip() + '\n' if new_line.strip() else '\n'

                # Append this *real* line to result_lines.
                s = lines[line_number]
                this_line = s[:column_number] + ' ' + s[column_number + 1:]
                result_lines.append(this_line.rstrip() + '\n' if this_line.strip() else '\n')

        # Set the result
        p.b = ''.join(result_lines).rstrip() + '\n'
    #@+node:ekr.20231022150805.1: *4* indented_i.remove_blank_lines
    def remove_blank_lines(self, p: Position) -> None:
        """Replace multiple blank lines with a single blank line."""
        if not p.b.strip():
            return
        result_lines = []
        for line in g.splitLines(p.b):
            if line.strip():
                result_lines.append(line)
            elif result_lines and result_lines[-1].strip():
                # A blank line preceded by a non-blank line.
                result_lines.append('\n')
        p.b =  p.b = ''.join(result_lines).rstrip() + '\n'
    #@+node:ekr.20231023045225.1: *4* indented_i.remove_first_block_comment
    def remove_first_block_comment(self, p: Position) -> None:
        """Remove the first block C comment."""
        if not p.b.strip():
            return
        lines = g.splitLines(p.b)
        if not lines[0].startswith('/*'):
            return
        for i, line in enumerate(lines):
            if line.strip().endswith('*/'):
                tail = lines[i + 1:]
                p.b = ''.join(tail).lstrip('\n')
                return
    #@+node:ekr.20231023044845.1: *4* indented_i.remove_includes
    def remove_includes(self, p: Position) -> None:
        """Remove #include lines."""
        if not p.b.strip():
            return
        lines = g.splitLines(p.b)
        result_lines = [z for z in lines if not z.startswith('#include ')]
        p.b =  p.b = ''.join(result_lines).rstrip() + '\n'
    #@+node:ekr.20231022152015.1: *4* indented_i.remove_trailing_semicolons
    def remove_trailing_semicolons(self, p: Position) -> None:

        if not p.b.strip():
            return
        lines = g.splitLines(p.b)
        result_lines = []
        for line in lines:
            line_s = line.rstrip()
            if line_s.endswith(';'):
                line = line_s[:-1] + '\n'
            result_lines.append(line)
        p.b =  p.b = ''.join(result_lines).rstrip() + '\n'
    #@+node:ekr.20231022150031.1: *3* indented_i.isAtFileNode & atFileName
    def isAtFileNode(self, p: Position) -> bool:
        h = p.h
        if h.startswith('@@'):
            h = h[1:]
        # Not complete.
        return h.startswith(('@auto ', '@clean ', '@edit ', '@file '))

    def atFileName(self, p: Position) -> str:
        assert self.isAtFileNode(p), repr(p.h)
        i = p.h.find(' ')
        assert i > -1, p.h
        return p.h[i:].strip()
    #@-others
#@+node:ekr.20231024024201.1: **  class Token
class Token:
    """
    A class reprenting a Lisp token.
    """
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value

    def __repr__(self):
        return f"Token: {self.kind!r}: {self.value!r}"

    __str__ = __repr__
    
    def to_string(self):
        return self.value
#@+node:ekr.20231022080007.1: ** class Indented_C
class Indented_C(Indented_Importer):
    """A class to support indented C files."""

    extensions: list[str] = ['.c', '.cpp', '.cc']
    importer_class = C_Importer
    language = 'c'
#@+node:ekr.20230917083456.1: ** class Indented_Lisp
class Indented_Lisp(Indented_Importer):
    """
    A class to support indented Lisp files.

    This class rearranges tokens. Guide lines won't work.
    """

    extensions: list[str] = ['.el', '.scm']
    importer_class = None  # There is no need for importer.make_guide_lines.
    language = 'lisp'
    operators = (
        # From lowest to highest precedence.
        'and', 'or',
        'max', 'min',
        '=', '<=', '>=', '/=',
        '+', '-',
        '*', '/',
        '%',
    )

    #@+others
    #@+node:ekr.20231024044903.1: *3* indented_lisp.convert_node (production)
    def convert_node(self, p: Position) -> None:
        """
        Convert from prefix to infix notation, removing parens if possible.
        """
        if not p.b.strip():
            return
        tokens = self.tokenize(p)
        output_list: list[str] = []
        level = 0
        at_start_of_line = True
        for i, token in enumerate(tokens):
            if token.kind == '(':
                at_start_of_line = False
                level += 1
                matching_i = self.find_matching_paren(i, tokens)
                if matching_i is not None:
                    # Null out only the *value* of both tokens.
                    matching_token = tokens[matching_i]
                    token.value = matching_token.value = ''
                    self.do_args(i, matching_i, tokens)
            elif token.kind == ')':
                at_start_of_line = False
                level -= 1
            elif token.kind == '\n':
                at_start_of_line = True
                output_list.append('\n')
                # output_list.append(f"level: {level}" + ' ' * 2 * level)
                output_list.append(' ' * 2 * level)
            elif token.kind == ' ':
                if not at_start_of_line:
                    output_list.append(' ')
            else:
                at_start_of_line = False
                output_list.append(token.value)

        p.b = ''.join(output_list)
        if 0:
            print('')
            print(p.h)
            print(''.join(output_list))
    #@+node:ekr.20231024103253.1: *4* indented_lisp.do_args
    def do_args(self, start: int, end: int, tokens: list[Token], level: int = 0) -> list[Token]:
        """
        Find and evaluate all args.
        Return the evaluated args as a flattened list of tokens.
        """

        # Prechecks.
        assert tokens[end].kind == ')'
        arg_tokens = tokens[start:end + 1]
        assert arg_tokens[0].kind == '(', repr(arg_tokens[0])
        assert arg_tokens[-1].kind == ')', repr(arg_tokens[-1])
        stripped_args = [z for z in arg_tokens if z.kind != ' ']

        # Handle each operator/symbol.
        args = stripped_args[1:-1]
        arg0 = args[0]
        op = arg0.value
        if op not in self.operators:
            return
        if 1:
            print('')
            # g.trace(f"args for {op} {start:>3}:{end:<3} {arg0.value!r}\n{self.to_string(args).rstrip()!s}\n")
            print(f"level: {level} op: '{op}' args: {self.to_string(args).rstrip()!s}")
        # Change the *value* from '=' to '=='.
        if arg0.kind == '=':
            arg0.value = '=='
        # Find all the inner args.
        inner_args: list[list[Token]] = []
        i = 1  # Skip the operator.
        while i < len(args):
            token = args[i]
            progress = i
            assert token.kind != ' ', (i, repr(token))
            if token.kind in ('\\', 'symbol', 'number'):
                inner_args.append([token])
                i += 1
            elif token.kind == '(':
                matching_i = self.find_matching_paren(i, args)
                if matching_i is None:
                    g.trace(f"Can not happen: no matching ')': {i}")
                    return
                # Recursively evaluate the inner arg.
                if 1:
                    # g.trace(i, matching_i, args[i:matching_i+ 1])
                    evaluated_args = self.do_args(i, matching_i, args, level=level+1)  ### args[i:matching_i + 1])
                    if evaluated_args:
                        inner_args.append(evaluated_args)
                else:
                    inner_args.append(args[i:matching_i + 1])
                i = matching_i + 1
            else:
                g.trace(f"Unexpected token: {i} {token!r}")
                return
            assert i > progress, (i, repr(token))
        if 1:
            print('\nInner args...')
            for n, inner_arg in enumerate(inner_args):
                print(f"inner arg: {n}: {self.to_string(inner_arg)}")
        # Flatten the list, embedding the op.
        result_list = []
        lt_token, rt_token = Token('(', '('), Token(')', ')')
        for inner_arg_n, inner_arg in enumerate(inner_args):
            if len(inner_arg) > 1:
                result_list.append(lt_token)
                result_list.extend(inner_arg)
                result_list.append(rt_token)
            else:
                result_list.extend(inner_arg)
            if inner_arg_n < len(inner_args) - 1:
                result_list.append(arg0)
        if 1:
            # g.printObj(result_list, tag='Results')
            print('Results:', self.to_string(result_list))
        return result_list
    #@+node:ekr.20231024045727.1: *4* indented_lisp.find_matching_paren
    def find_matching_paren(self, i: int, tokens: list[Token]) -> int:
        """Return the index of the matching closing parenthesis."""
        assert tokens[i].kind == '(', tokens[i]
        start_i = i
        i += 1
        level = 1
        while i < len(tokens):
            token = tokens[i]
            if token.kind == '(':
                level += 1
            elif token.kind == ')':
                level -= 1
                if level == 0:
                    return i
            i += 1
        # Give an error.
        tail_tokens = tokens[start_i:]
        tail_values = [z.value for z in tail_tokens]
        tail_s = ''.join(tail_values)[:20]
        g.trace('No matching close paren', start_i, tail_s, '\n')
        return None
    #@+node:ekr.20231024024032.1: *3* indented_lisp.indent_node (prototype)
    def indent_node(self, p: Position) -> None:
        """Indent p.b with 2-space indentation."""
        if not p.b.strip():
            return
        tokens = self.tokenize(p)
        level = 0  # Net number of parens.
        result_lines: list[str] = []
        this_line: list[str] = []
        # Prototype: Indent using paren level.
        for token in tokens:
            kind = token.kind
            this_line.append(token.value)
            if kind == '(':
                level += 1
            elif kind == ')':
                level -= 1
            elif kind == '\n':
                last_line = ''.join(this_line)
                result_lines.append(last_line if last_line.strip() else '\n')
                indent = ' ' * 2 * level
                this_line = [indent]
        # Include the last line.
        last_line = ''.join(this_line)
        if last_line.strip():
            result_lines.append(last_line)
        if 0:
            print('')
            print(''.join(result_lines))
        p.b = ''.join(result_lines)
    #@+node:ekr.20231024044536.1: *3* indented_lisp.indent_outline (top-level)
    def indent_outline(self, root: Position) -> None:
        """
        Indented_Lisp.indent_outline: Indent the body text of root and all its
        descendants.

        Called by indented_i.do_import.
        """
        for p in root.self_and_subtree():
            if p.b.strip():
                if 1:
                    # Convert prefix to infix.
                    self.convert_node(p)
                else:
                    # A prototype.
                    self.indent_node(p)
            self.remove_blank_lines(p)

        # Remove @path.
        if root.b.startswith('@path'):
            lines = g.splitLines(root.b)
            root.b = ''.join(lines[1:])

        # Remove the useless first block comment.
        self.remove_first_block_comment(root)

        # Append @language.
        if '@language' not in root.b:
            root.b = root.b.rstrip() + f"\n\n@language {self.language}\n"
    #@+node:ekr.20231026081944.1: *3* indented_lisp.to_string
    def to_string(self, tokens: list[Token]) -> str:
        """Convert a list of tokens to a string."""
        return ' '.join([z.to_string() for z in tokens or []])
    #@+node:ekr.20231024024109.1: *3* indented_lisp.tokenize
    def tokenize(self, p: Position) -> list[Token]:
        """Create p.b to a list of Lisp_Tokens."""
        # ; is the only comment delim.
        # " is the only string delim
        s = p.b
        tokens: list[Token] = []

        def is_symbol1(ch: str) -> bool:
            """Return True if ch can start a symbol."""
            return ch.isalpha() or ch == '_'

        def is_symbol(ch: str) -> bool:
            """Return True if ch is valid within a symbol."""
            # Approximate. This class treats "operators" separately.
            return ch.isalnum() or ch in '_-'

        # Tokenize character by character.
        i = 0
        while i < len(s):
            progress = i
            ch = s[i]
            if ch == '\\':
                # Skip the next character! The lisp colorizer appears to have a bug here.
                tokens.append(Token(ch, ch))
                i += 1
                if i < len(s):
                    ch = s[i]
                    tokens.append(Token(ch, ch))
                    i += 1
            elif ch == ';':  # Scan a comment.
                start = i
                i += 1
                while i < len(s) and s[i] != '\n':
                    i += 1
                tokens.append(Token(ch, s[start:i]))
            elif ch == '"':  # Scan a string.
                start = i
                i += 1
                while i < len(s):
                    if s[i] == '\\':
                        i += 2
                    elif s[i] == '"':
                        i += 1
                        break
                    else:
                        i += 1
                else:
                    g.es_print(f"{self.file_name}: Unterminated string in {p.h}")
                tokens.append(Token(ch, s[start:i]))
            elif ch in ' \n':  # Convert multiple blanks and newlines to a single blank.
                start = i
                i += 1
                while i < len(s) and s[i] in ' \n':
                    i += 1
                tokens.append(Token(' ', ' '))
            elif ch.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                tokens.append(Token('number', s[start:i]))
            elif ch == '|':  # Everything up to the matching '|' is part of the symbol!
                i += 1
                start = i
                while i < len(s) and s[i] != '|':
                    i += 1
                if i < len(s) and s[i] == '|':
                    tokens.append(Token('symbol', s[start:i]))
                else:
                    g.es_print(f"{self.file_name}: Unterminated '|' symbol in {p.h}")
            elif is_symbol1(ch):
                start = i
                i += 1
                while i < len(s) and is_symbol(s[i]):
                    i += 1
                tokens.append(Token('symbol', s[start:i]))
            else:  # Everything else gets its own token.
                i += 1
                tokens.append(Token(ch, ch))
            assert i > progress, (repr(ch), i, repr(s[i: i+20]))
        # g.printObj(tokens, tag='tokenize')
        return tokens
    #@-others
#@+node:ekr.20231022073306.1: ** class Indented_TypeScript
class Indented_TypeScript(Indented_Importer):
    """A class to support indented Typescript files."""

    extensions: list[str] = ['.ts',]
    language = 'typescript'
    importer_class = TS_Importer
#@-others
#@-leo
