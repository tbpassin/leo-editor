# Leo colorizer control file for lisp mode.
# This file is in the public domain.

# Properties for lisp mode.
properties = {
    "commentEnd": " |#",
    "commentStart": "#| ",
    "indentCloseBrackets": ")",
    "indentOpenBrackets": "(",
    "lineComment": ";",
    "lineUpClosingBracket": "false",
    "noWordSep": "_-+?:",
}

# Attributes dict for lisp_main ruleset.
lisp_main_attributes_dict = {
    "default": "null",
    "digit_re": "",
    "escape": "\\",
    "highlight_digits": "true",
    "ignore_case": "false",
    "no_word_sep": "_-+?:",
}

# Dictionary of attributes dictionaries for lisp mode.
attributesDictDict = {
    "lisp_main": lisp_main_attributes_dict,
}

# Keywords dict for lisp_main ruleset.
lisp_main_keywords_dict = {
    "*": "keyword3",
    "**": "keyword3",
    "***": "keyword3",
    "*break-on-signals*": "keyword3",
    "*compile-file-pathname*": "keyword3",
    "*compile-file-truename*": "keyword3",
    "*compile-print*": "keyword3",
    "*compile-verbose*": "keyword3",
    "*debug-io*": "keyword3",
    "*debugger-hook*": "keyword3",
    "*default-pathname-defaults*": "keyword3",
    "*error-output*": "keyword3",
    "*features*": "keyword3",
    "*gensym-counter*": "keyword3",
    "*load-pathname*": "keyword3",
    "*load-print*": "keyword3",
    "*load-truename*": "keyword3",
    "*load-verbose*": "keyword3",
    "*macroexpand-hook*": "keyword3",
    "*modules*": "keyword3",
    "*package*": "keyword3",
    "*print-array*": "keyword3",
    "*print-base*": "keyword3",
    "*print-case*": "keyword3",
    "*print-circle*": "keyword3",
    "*print-escape*": "keyword3",
    "*print-gensym*": "keyword3",
    "*print-length*": "keyword3",
    "*print-level*": "keyword3",
    "*print-lines*": "keyword3",
    "*print-miser-width*": "keyword3",
    "*print-pprint-dispatch*": "keyword3",
    "*print-pretty*": "keyword3",
    "*print-radix*": "keyword3",
    "*print-readably*": "keyword3",
    "*print-right-margin*": "keyword3",
    "*query-io*": "keyword3",
    "*random-state*": "keyword3",
    "*read-base*": "keyword3",
    "*read-default-float-format*": "keyword3",
    "*read-eval*": "keyword3",
    "*read-suppress*": "keyword3",
    "*readtable*": "keyword3",
    "*standard-input*": "keyword3",
    "*standard-output*": "keyword3",
    "*terminal-io*": "keyword3",
    "*trace-output*": "keyword3",
    "+": "keyword3",
    "++": "keyword3",
    "+++": "keyword3",
    "-": "keyword3",
    "/": "keyword3",
    "//": "keyword3",
    "///": "keyword3",
    "/=": "keyword3",
    "1+": "keyword3",
    "1-": "keyword3",
    "<": "keyword3",
    "=": "keyword3",
    ">": "keyword3",
    "abort": "keyword2",
    "abs": "keyword3",
    "acons": "keyword3",
    "acos": "keyword3",
    "acosh": "keyword3",
    "add-method": "keyword3",
    "adjoin": "keyword3",
    "adjust-array": "keyword3",
    "adjustable-array-p": "keyword3",
    "allocate-instance": "keyword3",
    "alpha-char-p": "keyword3",
    "alphanumericp": "keyword3",
    "and": "keyword3",
    "append": "keyword3",
    "apply": "keyword3",
    "apropos": "keyword3",
    "apropos-list": "keyword3",
    "aref": "keyword3",
    "arithmetic-error": "keyword3",
    "arithmetic-error-operands": "keyword3",
    "arithmetic-error-operation": "keyword3",
    "array": "keyword3",
    "array-dimension": "keyword3",
    "array-dimension-limit": "keyword3",
    "array-dimensions": "keyword3",
    "array-displacement": "keyword3",
    "array-element-type": "keyword3",
    "array-has-fill-pointer-p": "keyword3",
    "array-in-bounds-p": "keyword3",
    "array-rank": "keyword3",
    "array-rank-limit": "keyword3",
    "array-row-major-index": "keyword3",
    "array-total-size": "keyword3",
    "array-total-size-limit": "keyword3",
    "arrayp": "keyword3",
    "ash": "keyword3",
    "asin": "keyword3",
    "asinh": "keyword3",
    "assert": "keyword2",
    "assoc": "keyword3",
    "assoc-if": "keyword3",
    "assoc-if-not": "keyword3",
    "atan": "keyword3",
    "atanh": "keyword3",
    "atom": "keyword3",
    "base-char": "keyword3",
    "base-string": "keyword3",
    "bignum": "keyword3",
    "bit": "keyword3",
    "bit-and": "keyword3",
    "bit-andc1": "keyword3",
    "bit-andc2": "keyword3",
    "bit-eqv": "keyword3",
    "bit-ior": "keyword3",
    "bit-nand": "keyword3",
    "bit-nor": "keyword3",
    "bit-not": "keyword3",
    "bit-orc1": "keyword3",
    "bit-orc2": "keyword3",
    "bit-vector": "keyword3",
    "bit-vector-p": "keyword3",
    "bit-xor": "keyword3",
    "block": "keyword2",
    "boole": "keyword3",
    "boole-1": "keyword3",
    "boole-2": "keyword3",
    "boole-and": "keyword3",
    "boole-andc1": "keyword3",
    "boole-andc2": "keyword3",
    "boole-c1": "keyword3",
    "boole-c2": "keyword3",
    "boole-clr": "keyword3",
    "boole-eqv": "keyword3",
    "boole-ior": "keyword3",
    "boole-nand": "keyword3",
    "boole-nor": "keyword3",
    "boole-orc1": "keyword3",
    "boole-orc2": "keyword3",
    "boole-set": "keyword3",
    "boole-xor": "keyword3",
    "boolean": "keyword3",
    "both-case-p": "keyword3",
    "boundp": "keyword3",
    "break": "keyword2",
    "broadcast-stream": "keyword3",
    "broadcast-stream-streams": "keyword3",
    "built-in-class": "keyword3",
    "butlast": "keyword3",
    "byte": "keyword3",
    "byte-position": "keyword3",
    "byte-size": "keyword3",
    "caaaar": "keyword3",
    "caaadr": "keyword3",
    "caaar": "keyword3",
    "caadar": "keyword3",
    "caaddr": "keyword3",
    "caadr": "keyword3",
    "caar": "keyword3",
    "cadaar": "keyword3",
    "cadadr": "keyword3",
    "cadar": "keyword3",
    "caddar": "keyword3",
    "cadddr": "keyword3",
    "caddr": "keyword3",
    "cadr": "keyword3",
    "call-arguments-limit": "keyword3",
    "call-method": "keyword3",
    "call-next-method": "keyword3",
    "car": "keyword3",
    "case": "keyword2",
    "catch": "keyword2",
    "ccase": "keyword2",
    "cdaaar": "keyword3",
    "cdaadr": "keyword3",
    "cdaar": "keyword3",
    "cdadar": "keyword3",
    "cdaddr": "keyword3",
    "cdadr": "keyword3",
    "cdar": "keyword3",
    "cddaar": "keyword3",
    "cddadr": "keyword3",
    "cddar": "keyword3",
    "cdddar": "keyword3",
    "cddddr": "keyword3",
    "cdddr": "keyword3",
    "cddr": "keyword3",
    "cdr": "keyword3",
    "ceiling": "keyword3",
    "cell-error": "keyword3",
    "cell-error-name": "keyword3",
    "cerror": "keyword2",
    "change-class": "keyword3",
    "char": "keyword3",
    "char-code": "keyword3",
    "char-code-limit": "keyword3",
    "char-downcase": "keyword3",
    "char-equal": "keyword3",
    "char-greaterp": "keyword3",
    "char-int": "keyword3",
    "char-lessp": "keyword3",
    "char-name": "keyword3",
    "char-not-equal": "keyword3",
    "char-not-greaterp": "keyword3",
    "char-not-lessp": "keyword3",
    "char-upcase": "keyword3",
    "char/=": "keyword3",
    "char=": "keyword3",
    "character": "keyword3",
    "characterp": "keyword3",
    "check-type": "keyword3",
    "cis": "keyword3",
    "class": "keyword3",
    "class-name": "keyword3",
    "class-of": "keyword3",
    "clear-input": "keyword3",
    "clear-output": "keyword3",
    "close": "keyword3",
    "clrhash": "keyword3",
    "code-char": "keyword3",
    "coerce": "keyword3",
    "compilation-speed": "keyword3",
    "compile": "keyword3",
    "compile-file": "keyword3",
    "compile-file-pathname": "keyword3",
    "compiled-function": "keyword3",
    "compiled-function-p": "keyword3",
    "compiler-macro": "keyword3",
    "compiler-macro-function": "keyword3",
    "complement": "keyword3",
    "complex": "keyword3",
    "complexp": "keyword3",
    "compute-applicable-methods": "keyword3",
    "compute-restarts": "keyword3",
    "concatenate": "keyword3",
    "concatenated-stream": "keyword3",
    "concatenated-stream-streams": "keyword3",
    "cond": "keyword2",
    "condition": "keyword3",
    "conjugate": "keyword3",
    "cons": "keyword3",
    "consp": "keyword3",
    "constantly": "keyword3",
    "constantp": "keyword3",
    "continue": "keyword3",
    "control-error": "keyword3",
    "copy-alist": "keyword3",
    "copy-list": "keyword3",
    "copy-pprint-dispatch": "keyword3",
    "copy-readtable": "keyword3",
    "copy-seq": "keyword3",
    "copy-structure": "keyword3",
    "copy-symbol": "keyword3",
    "copy-tree": "keyword3",
    "cos": "keyword3",
    "cosh": "keyword3",
    "count": "keyword3",
    "count-if": "keyword3",
    "count-if-not": "keyword3",
    "ctypecase": "keyword2",
    "debug": "keyword3",
    "decf": "keyword3",
    "declaim": "keyword2",
    "declaration": "keyword3",
    "declare": "keyword2",
    "decode-float": "keyword3",
    "decode-universal-time": "keyword3",
    "defclass": "keyword1",
    "defconstant": "keyword1",
    "defgeneric": "keyword1",
    "define-compiler-macro": "keyword1",
    "define-condition": "keyword1",
    "define-method-combination": "keyword1",
    "define-modify-macro": "keyword1",
    "define-setf-expander": "keyword1",
    "define-symbol-macro": "keyword1",
    "defmacro": "keyword1",
    "defmethod": "keyword1",
    "defpackage": "keyword1",
    "defparameter": "keyword1",
    "defsetf": "keyword1",
    "defstruct": "keyword1",
    "deftype": "keyword1",
    "defun": "keyword1",
    "defvar": "keyword1",
    "delete": "keyword3",
    "delete-duplicates": "keyword3",
    "delete-file": "keyword3",
    "delete-if": "keyword3",
    "delete-if-not": "keyword3",
    "delete-package": "keyword3",
    "denominator": "keyword3",
    "deposit-field": "keyword3",
    "describe": "keyword3",
    "describe-object": "keyword3",
    "destructuring-bind": "keyword3",
    "digit-char": "keyword3",
    "digit-char-p": "keyword3",
    "directory": "keyword3",
    "directory-namestring": "keyword3",
    "disassemble": "keyword3",
    "division-by-zero": "keyword3",
    "do": "keyword2",
    "do*": "keyword2",
    "do-all-symbols": "keyword2",
    "do-external-symbols": "keyword2",
    "do-symbols": "keyword2",
    "documentation": "keyword3",
    "dolist": "keyword2",
    "dotimes": "keyword2",
    "double-float": "keyword3",
    "double-float-epsilon": "keyword3",
    "double-float-negative-epsilon": "keyword3",
    "dpb": "keyword3",
    "dribble": "keyword3",
    "dynamic-extent": "keyword3",
    "ecase": "keyword2",
    "echo-stream": "keyword3",
    "echo-stream-input-stream": "keyword3",
    "echo-stream-output-stream": "keyword3",
    "ed": "keyword3",
    "eighth": "keyword3",
    "elt": "keyword3",
    "encode-universal-time": "keyword3",
    "end-of-file": "keyword3",
    "endp": "keyword3",
    "enough-namestring": "keyword3",
    "ensure-directories-exist": "keyword3",
    "ensure-generic-function": "keyword3",
    "eq": "keyword3",
    "eql": "keyword3",
    "equal": "keyword3",
    "equalp": "keyword3",
    "error": "keyword2",
    "etypecase": "keyword2",
    "eval": "keyword3",
    "eval-when": "keyword2",
    "evenp": "keyword3",
    "every": "keyword3",
    "exp": "keyword3",
    "export": "keyword3",
    "expt": "keyword3",
    "extended-char": "keyword3",
    "fboundp": "keyword3",
    "fceiling": "keyword3",
    "fdefinition": "keyword3",
    "ffloor": "keyword3",
    "fifth": "keyword3",
    "file-author": "keyword3",
    "file-error": "keyword3",
    "file-error-pathname": "keyword3",
    "file-length": "keyword3",
    "file-namestring": "keyword3",
    "file-position": "keyword3",
    "file-stream": "keyword3",
    "file-string-length": "keyword3",
    "file-write-date": "keyword3",
    "fill": "keyword3",
    "fill-pointer": "keyword3",
    "find": "keyword3",
    "find-all-symbols": "keyword3",
    "find-class": "keyword3",
    "find-if": "keyword3",
    "find-if-not": "keyword3",
    "find-method": "keyword3",
    "find-package": "keyword3",
    "find-restart": "keyword3",
    "find-symbol": "keyword3",
    "finish-output": "keyword3",
    "first": "keyword3",
    "fixnum": "keyword3",
    "flet": "keyword2",
    "float": "keyword3",
    "float-digits": "keyword3",
    "float-precision": "keyword3",
    "float-radix": "keyword3",
    "float-sign": "keyword3",
    "floating-point-inexact": "keyword3",
    "floating-point-invalid-operation": "keyword3",
    "floating-point-overflow": "keyword3",
    "floating-point-underflow": "keyword3",
    "floatp": "keyword3",
    "floor": "keyword3",
    "fmakunbound": "keyword3",
    "force-output": "keyword3",
    "format": "keyword3",
    "formatter": "keyword3",
    "fourth": "keyword3",
    "fresh-line": "keyword3",
    "fround": "keyword3",
    "ftruncate": "keyword3",
    "ftype": "keyword3",
    "funcall": "keyword3",
    "function": "keyword3",
    "function-keywords": "keyword3",
    "function-lambda-expression": "keyword3",
    "functionp": "keyword3",
    "gcd": "keyword3",
    "generic-function": "keyword3",
    "gensym": "keyword3",
    "gentemp": "keyword3",
    "get": "keyword3",
    "get-decoded-time": "keyword3",
    "get-dispatch-macro-character": "keyword3",
    "get-internal-real-time": "keyword3",
    "get-internal-run-time": "keyword3",
    "get-macro-character": "keyword3",
    "get-output-stream-string": "keyword3",
    "get-properties": "keyword3",
    "get-setf-expansion": "keyword3",
    "get-universal-time": "keyword3",
    "getf": "keyword3",
    "gethash": "keyword3",
    "go": "keyword3",
    "graphic-char-p": "keyword3",
    "handler-bind": "keyword2",
    "handler-case": "keyword2",
    "hash-table": "keyword3",
    "hash-table-count": "keyword3",
    "hash-table-p": "keyword3",
    "hash-table-rehash-size": "keyword3",
    "hash-table-rehash-threshold": "keyword3",
    "hash-table-size": "keyword3",
    "hash-table-test": "keyword3",
    "host-namestring": "keyword3",
    "identity": "keyword3",
    "if": "keyword2",
    "ignorable": "keyword3",
    "ignore": "keyword3",
    "ignore-errors": "keyword2",
    "imagpart": "keyword3",
    "import": "keyword3",
    "in-package": "keyword2",
    "incf": "keyword3",
    "initialize-instance": "keyword3",
    "inline": "keyword3",
    "input-stream-p": "keyword3",
    "inspect": "keyword3",
    "integer": "keyword3",
    "integer-decode-float": "keyword3",
    "integer-length": "keyword3",
    "integerp": "keyword3",
    "interactive-stream-p": "keyword3",
    "intern": "keyword3",
    "internal-time-units-per-second": "keyword3",
    "intersection": "keyword3",
    "invalid-method-error": "keyword3",
    "invoke-debugger": "keyword3",
    "invoke-restart": "keyword3",
    "invoke-restart-interactively": "keyword3",
    "isqrt": "keyword3",
    "keyword": "keyword3",
    "keywordp": "keyword3",
    "labels": "keyword2",
    "lambda": "keyword2",
    "lambda-list-keywords": "keyword3",
    "lambda-parameters-limit": "keyword3",
    "last": "keyword3",
    "lcm": "keyword3",
    "ldb": "keyword3",
    "ldb-test": "keyword3",
    "ldiff": "keyword3",
    "least-negative-double-float": "keyword3",
    "least-negative-long-float": "keyword3",
    "least-negative-normalized-double-float": "keyword3",
    "least-negative-normalized-long-float": "keyword3",
    "least-negative-normalized-short-float": "keyword3",
    "least-negative-normalized-single-float": "keyword3",
    "least-negative-short-float": "keyword3",
    "least-negative-single-float": "keyword3",
    "least-positive-double-float": "keyword3",
    "least-positive-long-float": "keyword3",
    "least-positive-normalized-double-float": "keyword3",
    "least-positive-normalized-long-float": "keyword3",
    "least-positive-normalized-short-float": "keyword3",
    "least-positive-normalized-single-float": "keyword3",
    "least-positive-short-float": "keyword3",
    "least-positive-single-float": "keyword3",
    "length": "keyword3",
    "let": "keyword2",
    "let*": "keyword2",
    "lisp-implementation-type": "keyword3",
    "lisp-implementation-version": "keyword3",
    "list": "keyword3",
    "list*": "keyword3",
    "list-all-packages": "keyword3",
    "list-length": "keyword3",
    "listen": "keyword3",
    "listp": "keyword3",
    "load": "keyword3",
    "load-logical-pathname-translations": "keyword3",
    "load-time-value": "keyword3",
    "locally": "keyword2",
    "log": "keyword3",
    "logand": "keyword3",
    "logandc1": "keyword3",
    "logandc2": "keyword3",
    "logbitp": "keyword3",
    "logcount": "keyword3",
    "logeqv": "keyword3",
    "logical-pathname": "keyword3",
    "logical-pathname-translations": "keyword3",
    "logior": "keyword3",
    "lognand": "keyword3",
    "lognor": "keyword3",
    "lognot": "keyword3",
    "logorc1": "keyword3",
    "logorc2": "keyword3",
    "logtest": "keyword3",
    "logxor": "keyword3",
    "long-float": "keyword3",
    "long-float-epsilon": "keyword3",
    "long-float-negative-epsilon": "keyword3",
    "long-site-name": "keyword3",
    "loop": "keyword2",
    "loop-finish": "keyword3",
    "lower-case-p": "keyword3",
    "machine-instance": "keyword3",
    "machine-type": "keyword3",
    "machine-version": "keyword3",
    "macro-function": "keyword3",
    "macroexpand": "keyword3",
    "macroexpand-1": "keyword3",
    "macrolet": "keyword2",
    "make-array": "keyword3",
    "make-broadcast-stream": "keyword3",
    "make-concatenated-stream": "keyword3",
    "make-condition": "keyword3",
    "make-dispatch-macro-character": "keyword3",
    "make-echo-stream": "keyword3",
    "make-hash-table": "keyword3",
    "make-instance": "keyword3",
    "make-instances-obsolete": "keyword3",
    "make-list": "keyword3",
    "make-load-form": "keyword3",
    "make-load-form-saving-slots": "keyword3",
    "make-method": "keyword3",
    "make-package": "keyword3",
    "make-pathname": "keyword3",
    "make-random-state": "keyword3",
    "make-sequence": "keyword3",
    "make-string": "keyword3",
    "make-string-input-stream": "keyword3",
    "make-string-output-stream": "keyword3",
    "make-symbol": "keyword3",
    "make-synonym-stream": "keyword3",
    "make-two-way-stream": "keyword3",
    "makunbound": "keyword3",
    "map": "keyword3",
    "map-into": "keyword3",
    "mapc": "keyword3",
    "mapcan": "keyword3",
    "mapcar": "keyword3",
    "mapcon": "keyword3",
    "maphash": "keyword3",
    "mapl": "keyword3",
    "maplist": "keyword3",
    "mask-field": "keyword3",
    "max": "keyword3",
    "member": "keyword3",
    "member-if": "keyword3",
    "member-if-not": "keyword3",
    "merge": "keyword3",
    "merge-pathnames": "keyword3",
    "method": "keyword3",
    "method-combination": "keyword3",
    "method-combination-error": "keyword3",
    "method-qualifiers": "keyword3",
    "min": "keyword3",
    "minusp": "keyword3",
    "mismatch": "keyword3",
    "mod": "keyword3",
    "most-negative-double-float": "keyword3",
    "most-negative-fixnum": "keyword3",
    "most-negative-long-float": "keyword3",
    "most-negative-short-float": "keyword3",
    "most-negative-single-float": "keyword3",
    "most-positive-double-float": "keyword3",
    "most-positive-fixnum": "keyword3",
    "most-positive-long-float": "keyword3",
    "most-positive-short-float": "keyword3",
    "most-positive-single-float": "keyword3",
    "muffle-warning": "keyword3",
    "multiple-value-bind": "keyword2",
    "multiple-value-call": "keyword3",
    "multiple-value-list": "keyword3",
    "multiple-value-prog1": "keyword3",
    "multiple-value-setq": "keyword3",
    "multiple-values-limit": "keyword3",
    "name-char": "keyword3",
    "namestring": "keyword3",
    "nbutlast": "keyword3",
    "nconc": "keyword3",
    "next-method-p": "keyword3",
    "nil": "literal2",
    "nintersection": "keyword3",
    "ninth": "keyword3",
    "no-applicable-method": "keyword3",
    "no-next-method": "keyword3",
    "not": "keyword3",
    "notany": "keyword3",
    "notevery": "keyword3",
    "notinline": "keyword3",
    "nreconc": "keyword3",
    "nreverse": "keyword3",
    "nset-difference": "keyword3",
    "nset-exclusive-or": "keyword3",
    "nstring-capitalize": "keyword3",
    "nstring-downcase": "keyword3",
    "nstring-upcase": "keyword3",
    "nsublis": "keyword3",
    "nsubst": "keyword3",
    "nsubst-if": "keyword3",
    "nsubst-if-not": "keyword3",
    "nsubstitute": "keyword3",
    "nsubstitute-if": "keyword3",
    "nsubstitute-if-not": "keyword3",
    "nth": "keyword3",
    "nth-value": "keyword3",
    "nthcdr": "keyword3",
    "null": "keyword3",
    "number": "keyword3",
    "numberp": "keyword3",
    "numerator": "keyword3",
    "nunion": "keyword3",
    "oddp": "keyword3",
    "open": "keyword3",
    "open-stream-p": "keyword3",
    "optimize": "keyword3",
    "or": "keyword3",
    "otherwise": "keyword3",
    "output-stream-p": "keyword3",
    "package": "keyword3",
    "package-error": "keyword3",
    "package-error-package": "keyword3",
    "package-name": "keyword3",
    "package-nicknames": "keyword3",
    "package-shadowing-symbols": "keyword3",
    "package-use-list": "keyword3",
    "package-used-by-list": "keyword3",
    "packagep": "keyword3",
    "pairlis": "keyword3",
    "parse-error": "keyword3",
    "parse-integer": "keyword3",
    "parse-namestring": "keyword3",
    "pathname": "keyword3",
    "pathname-device": "keyword3",
    "pathname-directory": "keyword3",
    "pathname-host": "keyword3",
    "pathname-match-p": "keyword3",
    "pathname-name": "keyword3",
    "pathname-type": "keyword3",
    "pathname-version": "keyword3",
    "pathnamep": "keyword3",
    "peek-char": "keyword3",
    "phase": "keyword3",
    "pi": "keyword3",
    "plusp": "keyword3",
    "pop": "keyword3",
    "position": "keyword3",
    "position-if": "keyword3",
    "position-if-not": "keyword3",
    "pprint": "keyword3",
    "pprint-dispatch": "keyword3",
    "pprint-exit-if-list-exhausted": "keyword3",
    "pprint-fill": "keyword3",
    "pprint-indent": "keyword3",
    "pprint-linear": "keyword3",
    "pprint-logical-block": "keyword3",
    "pprint-newline": "keyword3",
    "pprint-pop": "keyword3",
    "pprint-tab": "keyword3",
    "pprint-tabular": "keyword3",
    "prin1": "keyword3",
    "prin1-to-string": "keyword3",
    "princ": "keyword3",
    "princ-to-string": "keyword3",
    "print": "keyword3",
    "print-not-readable": "keyword3",
    "print-not-readable-object": "keyword3",
    "print-object": "keyword3",
    "print-unreadable-object": "keyword3",
    "probe-file": "keyword3",
    "proclaim": "keyword2",
    "prog": "keyword2",
    "prog*": "keyword2",
    "prog1": "keyword2",
    "prog2": "keyword2",
    "progn": "keyword2",
    "program-error": "keyword3",
    "progv": "keyword2",
    "provide": "keyword2",
    "psetf": "keyword3",
    "psetq": "keyword3",
    "push": "keyword3",
    "pushnew": "keyword3",
    "quote": "keyword3",
    "random": "keyword3",
    "random-state": "keyword3",
    "random-state-p": "keyword3",
    "rassoc": "keyword3",
    "rassoc-if": "keyword3",
    "rassoc-if-not": "keyword3",
    "ratio": "keyword3",
    "rational": "keyword3",
    "rationalize": "keyword3",
    "rationalp": "keyword3",
    "read": "keyword3",
    "read-byte": "keyword3",
    "read-char": "keyword3",
    "read-char-no-hang": "keyword3",
    "read-delimited-list": "keyword3",
    "read-from-string": "keyword3",
    "read-line": "keyword3",
    "read-preserving-whitespace": "keyword3",
    "read-sequence": "keyword3",
    "reader-error": "keyword3",
    "readtable": "keyword3",
    "readtable-case": "keyword3",
    "readtablep": "keyword3",
    "real": "keyword3",
    "realp": "keyword3",
    "realpart": "keyword3",
    "reduce": "keyword3",
    "reinitialize-instance": "keyword3",
    "rem": "keyword3",
    "remf": "keyword3",
    "remhash": "keyword3",
    "remove": "keyword3",
    "remove-duplicates": "keyword3",
    "remove-if": "keyword3",
    "remove-if-not": "keyword3",
    "remove-method": "keyword3",
    "remprop": "keyword3",
    "rename-file": "keyword3",
    "rename-package": "keyword3",
    "replace": "keyword3",
    "require": "keyword2",
    "rest": "keyword3",
    "restart": "keyword3",
    "restart-bind": "keyword2",
    "restart-case": "keyword2",
    "restart-name": "keyword2",
    "return": "keyword2",
    "return-from": "keyword2",
    "revappend": "keyword3",
    "reverse": "keyword3",
    "room": "keyword3",
    "rotatef": "keyword3",
    "round": "keyword3",
    "row-major-aref": "keyword3",
    "rplaca": "keyword3",
    "rplacd": "keyword3",
    "safety": "keyword3",
    "satisfies": "keyword3",
    "sbit": "keyword3",
    "scale-float": "keyword3",
    "schar": "keyword3",
    "search": "keyword3",
    "second": "keyword3",
    "sequence": "keyword3",
    "serious-condition": "keyword3",
    "set": "keyword3",
    "set-difference": "keyword3",
    "set-dispatch-macro-character": "keyword3",
    "set-exclusive-or": "keyword3",
    "set-macro-character": "keyword3",
    "set-pprint-dispatch": "keyword3",
    "set-syntax-from-char": "keyword3",
    "setf": "keyword3",
    "setq": "keyword3",
    "seventh": "keyword3",
    "shadow": "keyword3",
    "shadowing-import": "keyword3",
    "shared-initialize": "keyword3",
    "shiftf": "keyword3",
    "short-float": "keyword3",
    "short-float-epsilon": "keyword3",
    "short-float-negative-epsilon": "keyword3",
    "short-site-name": "keyword3",
    "signal": "keyword2",
    "signed-byte": "keyword3",
    "signum": "keyword3",
    "simple-array": "keyword3",
    "simple-base-string": "keyword3",
    "simple-bit-vector": "keyword3",
    "simple-bit-vector-p": "keyword3",
    "simple-condition": "keyword3",
    "simple-condition-format-arguments": "keyword3",
    "simple-condition-format-control": "keyword3",
    "simple-error": "keyword3",
    "simple-string": "keyword3",
    "simple-string-p": "keyword3",
    "simple-type-error": "keyword3",
    "simple-vector": "keyword3",
    "simple-vector-p": "keyword3",
    "simple-warning": "keyword3",
    "sin": "keyword3",
    "single-float": "keyword3",
    "single-float-epsilon": "keyword3",
    "single-float-negative-epsilon": "keyword3",
    "sinh": "keyword3",
    "sixth": "keyword3",
    "sleep": "keyword3",
    "slot-boundp": "keyword3",
    "slot-exists-p": "keyword3",
    "slot-makunbound": "keyword3",
    "slot-missing": "keyword3",
    "slot-unbound": "keyword3",
    "slot-value": "keyword3",
    "software-type": "keyword3",
    "software-version": "keyword3",
    "some": "keyword3",
    "sort": "keyword3",
    "space": "keyword3",
    "special": "keyword3",
    "special-operator-p": "keyword3",
    "speed": "keyword3",
    "sqrt": "keyword3",
    "stable-sort": "keyword3",
    "standard": "keyword3",
    "standard-char": "keyword3",
    "standard-char-p": "keyword3",
    "standard-class": "keyword3",
    "standard-generic-function": "keyword3",
    "standard-method": "keyword3",
    "standard-object": "keyword3",
    "step": "keyword3",
    "storage-condition": "keyword3",
    "store-value": "keyword3",
    "stream": "keyword3",
    "stream-element-type": "keyword3",
    "stream-error": "keyword3",
    "stream-error-stream": "keyword3",
    "stream-external-format": "keyword3",
    "streamp": "keyword3",
    "string": "keyword3",
    "string-capitalize": "keyword3",
    "string-downcase": "keyword3",
    "string-equal": "keyword3",
    "string-greaterp": "keyword3",
    "string-left-trim": "keyword3",
    "string-lessp": "keyword3",
    "string-not-equal": "keyword3",
    "string-not-greaterp": "keyword3",
    "string-not-lessp": "keyword3",
    "string-right-trim": "keyword3",
    "string-stream": "keyword3",
    "string-trim": "keyword3",
    "string-upcase": "keyword3",
    "string/=": "keyword3",
    "string=": "keyword3",
    "stringp": "keyword3",
    "structure": "keyword3",
    "structure-class": "keyword3",
    "structure-object": "keyword3",
    "style-warning": "keyword3",
    "sublis": "keyword3",
    "subseq": "keyword3",
    "subsetp": "keyword3",
    "subst": "keyword3",
    "subst-if": "keyword3",
    "subst-if-not": "keyword3",
    "substitute": "keyword3",
    "substitute-if": "keyword3",
    "substitute-if-not": "keyword3",
    "subtypep": "keyword3",
    "svref": "keyword3",
    "sxhash": "keyword3",
    "symbol": "keyword3",
    "symbol-function": "keyword3",
    "symbol-macrolet": "keyword2",
    "symbol-name": "keyword3",
    "symbol-package": "keyword3",
    "symbol-plist": "keyword3",
    "symbol-value": "keyword3",
    "symbolp": "keyword3",
    "synonym-stream": "keyword3",
    "synonym-stream-symbol": "keyword3",
    "t": "literal2",
    "tagbody": "keyword2",
    "tailp": "keyword3",
    "tan": "keyword3",
    "tanh": "keyword3",
    "tenth": "keyword3",
    "terpri": "keyword3",
    "the": "keyword2",
    "third": "keyword3",
    "throw": "keyword2",
    "time": "keyword3",
    "trace": "keyword3",
    "translate-logical-pathname": "keyword3",
    "translate-pathname": "keyword3",
    "tree-equal": "keyword3",
    "truename": "keyword3",
    "truncate": "keyword3",
    "two-way-stream": "keyword3",
    "two-way-stream-input-stream": "keyword3",
    "two-way-stream-output-stream": "keyword3",
    "type": "keyword3",
    "type-error": "keyword3",
    "type-error-datum": "keyword3",
    "type-error-expected-type": "keyword3",
    "type-of": "keyword3",
    "typecase": "keyword2",
    "typep": "keyword3",
    "unbound-slot": "keyword3",
    "unbound-slot-instance": "keyword3",
    "unbound-variable": "keyword3",
    "undefined-function": "keyword3",
    "unexport": "keyword3",
    "unintern": "keyword3",
    "union": "keyword3",
    "unless": "keyword2",
    "unread-char": "keyword3",
    "unsigned-byte": "keyword3",
    "untrace": "keyword3",
    "unuse-package": "keyword3",
    "unwind-protect": "keyword2",
    "update-instance-for-different-class": "keyword3",
    "update-instance-for-redefined-class": "keyword3",
    "upgraded-array-element-type": "keyword3",
    "upgraded-complex-part-type": "keyword3",
    "upper-case-p": "keyword3",
    "use-package": "keyword3",
    "use-value": "keyword3",
    "user-homedir-pathname": "keyword3",
    "values": "keyword3",
    "values-list": "keyword3",
    "variable": "keyword3",
    "vector": "keyword3",
    "vector-pop": "keyword3",
    "vector-push": "keyword3",
    "vector-push-extend": "keyword3",
    "vectorp": "keyword3",
    "warn": "keyword3",
    "warning": "keyword3",
    "when": "keyword2",
    "wild-pathname-p": "keyword3",
    "with-accessors": "keyword2",
    "with-compilation-unit": "keyword2",
    "with-condition-restarts": "keyword2",
    "with-hash-table-iterator": "keyword2",
    "with-input-from-string": "keyword2",
    "with-open-file": "keyword2",
    "with-open-stream": "keyword2",
    "with-output-to-string": "keyword2",
    "with-package-iterator": "keyword2",
    "with-simple-restart": "keyword2",
    "with-slots": "keyword2",
    "with-standard-io-syntax": "keyword2",
    "write": "keyword3",
    "write-byte": "keyword3",
    "write-char": "keyword3",
    "write-line": "keyword3",
    "write-sequence": "keyword3",
    "write-string": "keyword3",
    "write-to-string": "keyword3",
    "y-or-n-p": "keyword3",
    "yes-or-no-p": "keyword3",
    "zerop": "keyword3",
}

# Dictionary of keywords dictionaries for lisp mode.
keywordsDictDict = {
    "lisp_main": lisp_main_keywords_dict,
}

# Rules for lisp_main ruleset.

def lisp_rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="#|", end="|#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def lisp_rule1(colorer, s, i):
    return colorer.match_seq(s, i, kind="null", seq="'(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def lisp_rule2(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="literal1", pattern="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def lisp_rule3(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword4", pattern="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def lisp_rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="`",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def lisp_rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="@",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def lisp_rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def lisp_rule7(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment4", seq=";;;;",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def lisp_rule8(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment3", seq=";;;",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def lisp_rule9(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq=";;",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def lisp_rule10(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def lisp_rule11(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def lisp_rule12(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for lisp_main ruleset.
rulesDict1 = {
    "\"": [lisp_rule11,],
    "#": [lisp_rule0,],
    "%": [lisp_rule6,],
    "&": [lisp_rule3,],
    "'": [lisp_rule1, lisp_rule2,],
    "*": [lisp_rule12,],
    "+": [lisp_rule12,],
    "-": [lisp_rule12,],
    "/": [lisp_rule12,],
    "0": [lisp_rule12,],
    "1": [lisp_rule12,],
    "2": [lisp_rule12,],
    "3": [lisp_rule12,],
    "4": [lisp_rule12,],
    "5": [lisp_rule12,],
    "6": [lisp_rule12,],
    "7": [lisp_rule12,],
    "8": [lisp_rule12,],
    "9": [lisp_rule12,],
    ";": [lisp_rule7, lisp_rule8, lisp_rule9, lisp_rule10,],
    "<": [lisp_rule12,],
    "=": [lisp_rule12,],
    ">": [lisp_rule12,],
    "@": [lisp_rule5, lisp_rule12,],
    "A": [lisp_rule12,],
    "B": [lisp_rule12,],
    "C": [lisp_rule12,],
    "D": [lisp_rule12,],
    "E": [lisp_rule12,],
    "F": [lisp_rule12,],
    "G": [lisp_rule12,],
    "H": [lisp_rule12,],
    "I": [lisp_rule12,],
    "J": [lisp_rule12,],
    "K": [lisp_rule12,],
    "L": [lisp_rule12,],
    "M": [lisp_rule12,],
    "N": [lisp_rule12,],
    "O": [lisp_rule12,],
    "P": [lisp_rule12,],
    "Q": [lisp_rule12,],
    "R": [lisp_rule12,],
    "S": [lisp_rule12,],
    "T": [lisp_rule12,],
    "U": [lisp_rule12,],
    "V": [lisp_rule12,],
    "W": [lisp_rule12,],
    "X": [lisp_rule12,],
    "Y": [lisp_rule12,],
    "Z": [lisp_rule12,],
    "`": [lisp_rule4,],
    "a": [lisp_rule12,],
    "b": [lisp_rule12,],
    "c": [lisp_rule12,],
    "d": [lisp_rule12,],
    "e": [lisp_rule12,],
    "f": [lisp_rule12,],
    "g": [lisp_rule12,],
    "h": [lisp_rule12,],
    "i": [lisp_rule12,],
    "j": [lisp_rule12,],
    "k": [lisp_rule12,],
    "l": [lisp_rule12,],
    "m": [lisp_rule12,],
    "n": [lisp_rule12,],
    "o": [lisp_rule12,],
    "p": [lisp_rule12,],
    "q": [lisp_rule12,],
    "r": [lisp_rule12,],
    "s": [lisp_rule12,],
    "t": [lisp_rule12,],
    "u": [lisp_rule12,],
    "v": [lisp_rule12,],
    "w": [lisp_rule12,],
    "x": [lisp_rule12,],
    "y": [lisp_rule12,],
    "z": [lisp_rule12,],
}

# x.rulesDictDict for lisp mode.
rulesDictDict = {
    "lisp_main": rulesDict1,
}

# Import dict for lisp mode.
importDict = {}
