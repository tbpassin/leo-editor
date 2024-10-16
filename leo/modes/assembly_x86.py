# Leo colorizer control file for assembly_x86 mode.
# This file is in the public domain.

# Properties for assembly_x86 mode.
properties = {
    "lineComment": ";",
}

# Attributes dict for assembly_x86_main ruleset.
assembly_x86_main_attributes_dict = {
    "default": "null",
    "digit_re": "",
    "escape": "",
    "highlight_digits": "true",
    "ignore_case": "true",
    "no_word_sep": "",
}

# Dictionary of attributes dictionaries for assembly_x86 mode.
attributesDictDict = {
    "assembly_x86_main": assembly_x86_main_attributes_dict,
}

# Keywords dict for assembly_x86_main ruleset.
assembly_x86_main_keywords_dict = {
    ".186": "keyword1",
    ".286": "keyword1",
    ".286p": "keyword1",
    ".287": "keyword1",
    ".386": "keyword1",
    ".386p": "keyword1",
    ".387": "keyword1",
    ".486": "keyword1",
    ".486p": "keyword1",
    ".586": "keyword1",
    ".586p": "keyword1",
    ".686": "keyword1",
    ".686p": "keyword1",
    ".8086": "keyword1",
    ".8087": "keyword1",
    ".alpha": "keyword1",
    ".break": "keyword1",
    ".bss": "keyword1",
    ".code": "keyword1",
    ".const": "keyword1",
    ".continue": "keyword1",
    ".cref": "keyword1",
    ".data": "keyword1",
    ".data?": "keyword1",
    ".dosseg": "keyword1",
    ".else": "keyword1",
    ".elseif": "keyword1",
    ".endif": "keyword1",
    ".endw": "keyword1",
    ".err": "keyword1",
    ".err1": "keyword1",
    ".err2": "keyword1",
    ".errb": "keyword1",
    ".errdef": "keyword1",
    ".errdif": "keyword1",
    ".errdifi": "keyword1",
    ".erre": "keyword1",
    ".erridn": "keyword1",
    ".erridni": "keyword1",
    ".errnb": "keyword1",
    ".errndef": "keyword1",
    ".errnz": "keyword1",
    ".exit": "keyword1",
    ".fardata": "keyword1",
    ".fardata?": "keyword1",
    ".if": "keyword1",
    ".k3d": "keyword1",
    ".lall": "keyword1",
    ".lfcond": "keyword1",
    ".list": "keyword1",
    ".listall": "keyword1",
    ".listif": "keyword1",
    ".listmacro": "keyword1",
    ".listmacroall": "keyword1",
    ".mmx": "keyword1",
    ".model": "keyword1",
    ".msfloat": "keyword1",
    ".no87": "keyword1",
    ".nocref": "keyword1",
    ".nolist": "keyword1",
    ".nolistif": "keyword1",
    ".nolistmacro": "keyword1",
    ".radix": "keyword1",
    ".repeat": "keyword1",
    ".sall": "keyword1",
    ".seq": "keyword1",
    ".sfcond": "keyword1",
    ".stack": "keyword1",
    ".startup": "keyword1",
    ".text": "keyword1",
    ".tfcond": "keyword1",
    ".until": "keyword1",
    ".untilcxz": "keyword1",
    ".while": "keyword1",
    ".xall": "keyword1",
    ".xcref": "keyword1",
    ".xlist": "keyword1",
    ".xmm": "keyword1",
    "__file__": "keyword1",
    "__line__": "keyword1",
    "a16": "keyword1",
    "a32": "keyword1",
    "aaa": "function",
    "aad": "function",
    "aam": "function",
    "aas": "function",
    "adc": "function",
    "add": "function",
    "addps": "function",
    "addr": "keyword1",
    "addss": "function",
    "ah": "keyword3",
    "al": "keyword3",
    "align": "keyword1",
    "alignb": "keyword1",
    "and": "function",
    "andnps": "function",
    "andps": "function",
    "arpl": "function",
    "assume": "keyword1",
    "ax": "keyword3",
    "bh": "keyword3",
    "bits": "keyword1",
    "bl": "keyword3",
    "bound": "function",
    "bp": "keyword3",
    "bsf": "function",
    "bsr": "function",
    "bswap": "function",
    "bt": "function",
    "btc": "function",
    "btr": "function",
    "bts": "function",
    "bx": "keyword3",
    "byte": "keyword2",
    "call": "function",
    "carry?": "keyword1",
    "catstr": "keyword1",
    "cbw": "function",
    "cdq": "function",
    "ch": "keyword3",
    "cl": "keyword3",
    "clc": "function",
    "cld": "function",
    "cli": "function",
    "clts": "function",
    "cmc": "function",
    "cmova": "function",
    "cmovae": "function",
    "cmovb": "function",
    "cmovbe": "function",
    "cmovc": "function",
    "cmove": "function",
    "cmovg": "function",
    "cmovge": "function",
    "cmovl": "function",
    "cmovle": "function",
    "cmovna": "function",
    "cmovnae": "function",
    "cmovnb": "function",
    "cmovnbe": "function",
    "cmovnc": "function",
    "cmovne": "function",
    "cmovng": "function",
    "cmovnge": "function",
    "cmovnl": "function",
    "cmovnle": "function",
    "cmovno": "function",
    "cmovnp": "function",
    "cmovns": "function",
    "cmovnz": "function",
    "cmovo": "function",
    "cmovp": "function",
    "cmovpe": "function",
    "cmovpo": "function",
    "cmovs": "function",
    "cmovz": "function",
    "cmp": "function",
    "cmpps": "function",
    "cmps": "function",
    "cmpsb": "function",
    "cmpsd": "function",
    "cmpss": "function",
    "cmpsw": "function",
    "cmpxchg": "function",
    "cmpxchgb": "function",
    "codeseg": "keyword1",
    "comiss": "function",
    "comm": "keyword1",
    "comment": "keyword1",
    "common": "keyword1",
    "cpuid": "function",
    "cr0": "keyword3",
    "cr2": "keyword3",
    "cr3": "keyword3",
    "cr4": "keyword3",
    "cs": "keyword3",
    "cvtpi2ps": "function",
    "cvtps2pi": "function",
    "cvtsi2ss": "function",
    "cvtss2si": "function",
    "cvttps2pi": "function",
    "cvttss2si": "function",
    "cwd": "function",
    "cwde": "function",
    "cx": "keyword3",
    "daa": "function",
    "das": "function",
    "dataseg": "keyword1",
    "db": "keyword2",
    "dd": "keyword2",
    "dec": "function",
    "df": "keyword2",
    "dh": "keyword3",
    "di": "keyword3",
    "div": "function",
    "divps": "function",
    "divss": "function",
    "dl": "keyword3",
    "dosseg": "keyword1",
    "dq": "keyword2",
    "dr0": "keyword3",
    "dr1": "keyword3",
    "dr2": "keyword3",
    "dr3": "keyword3",
    "dr4": "keyword3",
    "dr5": "keyword3",
    "dr6": "keyword3",
    "dr7": "keyword3",
    "ds": "keyword3",
    "dt": "keyword2",
    "dup": "keyword2",
    "dw": "keyword2",
    "dword": "keyword2",
    "dx": "keyword3",
    "eax": "keyword3",
    "ebp": "keyword3",
    "ebx": "keyword3",
    "echo": "keyword1",
    "ecx": "keyword3",
    "edi": "keyword3",
    "edx": "keyword3",
    "else": "keyword1",
    "elseif": "keyword1",
    "elseif1": "keyword1",
    "elseif2": "keyword1",
    "elseifb": "keyword1",
    "elseifdef": "keyword1",
    "elseife": "keyword1",
    "elseifidn": "keyword1",
    "elseifnb": "keyword1",
    "elseifndef": "keyword1",
    "emms": "function",
    "end": "keyword1",
    "endif": "keyword1",
    "endm": "keyword1",
    "endp": "keyword1",
    "ends": "keyword1",
    "endstruc": "keyword1",
    "enter": "function",
    "equ": "keyword2",
    "es": "keyword3",
    "esi": "keyword3",
    "esp": "keyword3",
    "even": "keyword1",
    "exitm": "keyword1",
    "export": "keyword1",
    "extern": "keyword1",
    "externdef": "keyword1",
    "extrn": "keyword1",
    "f2xm1": "function",
    "fabs": "function",
    "fadd": "function",
    "faddp": "function",
    "far": "keyword1",
    "fbld": "function",
    "fbstp": "function",
    "fchs": "function",
    "fclex": "function",
    "fcmovb": "function",
    "fcmovbe": "function",
    "fcmove": "function",
    "fcmovnb": "function",
    "fcmovnbe": "function",
    "fcmovne": "function",
    "fcmovnu": "function",
    "fcmovu": "function",
    "fcom": "function",
    "fcomi": "function",
    "fcomip": "function",
    "fcomp": "function",
    "fcompp": "function",
    "fcos": "function",
    "fdecstp": "function",
    "fdiv": "function",
    "fdivp": "function",
    "fdivr": "function",
    "fdivrp": "function",
    "femms": "function",
    "ffree": "function",
    "fiadd": "function",
    "ficom": "function",
    "ficomp": "function",
    "fidiv": "function",
    "fidivr": "function",
    "fild": "function",
    "fimul": "function",
    "fincstp": "function",
    "finit": "function",
    "fist": "function",
    "fistp": "function",
    "fisub": "function",
    "fisubr": "function",
    "fld1": "function",
    "fldcw": "function",
    "fldenv": "function",
    "fldl2e": "function",
    "fldl2t": "function",
    "fldlg2": "function",
    "fldln2": "function",
    "fldpi": "function",
    "fldz": "function",
    "fmul": "function",
    "fmulp": "function",
    "fnclex": "function",
    "fninit": "function",
    "fnop": "function",
    "fnsave": "function",
    "fnstcw": "function",
    "fnstenv": "function",
    "fnstsw": "function",
    "for": "keyword1",
    "forc": "keyword1",
    "fpatan": "function",
    "fprem": "function",
    "fpremi": "function",
    "fptan": "function",
    "frndint": "function",
    "frstor": "function",
    "fs": "keyword3",
    "fsave": "function",
    "fscale": "function",
    "fsin": "function",
    "fsincos": "function",
    "fsqrt": "function",
    "fst": "function",
    "fstcw": "function",
    "fstenv": "function",
    "fstp": "function",
    "fstsw": "function",
    "fsub": "function",
    "fsubp": "function",
    "fsubr": "function",
    "fsubrp": "function",
    "ftst": "function",
    "fucom": "function",
    "fucomi": "function",
    "fucomip": "function",
    "fucomp": "function",
    "fucompp": "function",
    "fwait": "function",
    "fword": "keyword2",
    "fxam": "function",
    "fxch": "function",
    "fxrstor": "function",
    "fxsave": "function",
    "fxtract": "function",
    "fyl2x": "function",
    "fyl2xp1": "function",
    "global": "keyword1",
    "goto": "keyword1",
    "group": "keyword1",
    "gs": "keyword3",
    "high": "keyword1",
    "highword": "keyword1",
    "hlt": "function",
    "idiv": "function",
    "iend": "keyword1",
    "if": "keyword1",
    "if1": "keyword1",
    "if2": "keyword1",
    "ifb": "keyword1",
    "ifdef": "keyword1",
    "ifdif": "keyword1",
    "ifdifi": "keyword1",
    "ife": "keyword1",
    "ifidn": "keyword1",
    "ifidni": "keyword1",
    "ifnb": "keyword1",
    "ifndef": "keyword1",
    "import": "keyword1",
    "imul": "function",
    "in": "function",
    "inc": "function",
    "incbin": "keyword1",
    "include": "keyword1",
    "includelib": "keyword1",
    "ins": "function",
    "insb": "function",
    "insd": "function",
    "instr": "keyword1",
    "insw": "function",
    "int": "function",
    "into": "function",
    "invd": "function",
    "invlpg": "function",
    "invoke": "keyword1",
    "iret": "function",
    "irp": "keyword1",
    "irpc": "keyword1",
    "istruc": "keyword1",
    "ja": "function",
    "jae": "function",
    "jb": "function",
    "jbe": "function",
    "jc": "function",
    "jcxz": "function",
    "je": "function",
    "jecxz": "function",
    "jg": "function",
    "jge": "function",
    "jl": "function",
    "jle": "function",
    "jmp": "function",
    "jna": "function",
    "jnae": "function",
    "jnb": "function",
    "jnbe": "function",
    "jnc": "function",
    "jne": "function",
    "jng": "function",
    "jnge": "function",
    "jnl": "function",
    "jnle": "function",
    "jno": "function",
    "jnp": "function",
    "jns": "function",
    "jnz": "function",
    "jo": "function",
    "jp": "function",
    "jpe": "function",
    "jpo": "function",
    "js": "function",
    "jz": "function",
    "label": "keyword1",
    "lahf": "function",
    "lar": "function",
    "ldmxcsr": "function",
    "lds": "function",
    "lea": "function",
    "leave": "function",
    "length": "keyword1",
    "lengthof": "keyword1",
    "les": "function",
    "lfs": "function",
    "lgdt": "function",
    "lgs": "function",
    "lidt": "function",
    "lldt": "function",
    "lmsw": "function",
    "local": "keyword1",
    "lock": "function",
    "lods": "function",
    "lodsb": "function",
    "lodsd": "function",
    "lodsw": "function",
    "loop": "function",
    "loope": "function",
    "loopne": "function",
    "loopnz": "function",
    "loopz": "function",
    "low": "keyword1",
    "lowword": "keyword1",
    "lroffset": "keyword1",
    "lsl": "function",
    "lss": "function",
    "ltr": "function",
    "macro": "keyword1",
    "maskmovq": "function",
    "maxps": "function",
    "maxss": "function",
    "minps": "function",
    "minss": "function",
    "mm0": "keyword3",
    "mm1": "keyword3",
    "mm2": "keyword3",
    "mm3": "keyword3",
    "mm4": "keyword3",
    "mm5": "keyword3",
    "mm6": "keyword3",
    "mm7": "keyword3",
    "mov": "function",
    "movaps": "function",
    "movd": "function",
    "movhlps": "function",
    "movhps": "function",
    "movlhps": "function",
    "movlps": "function",
    "movmskps": "function",
    "movntps": "function",
    "movntq": "function",
    "movq": "function",
    "movs": "function",
    "movsb": "function",
    "movsd": "function",
    "movss": "function",
    "movsw": "function",
    "movsx": "function",
    "movups": "function",
    "movzx": "function",
    "mul": "function",
    "mulps": "function",
    "mulss": "function",
    "name": "keyword1",
    "near": "keyword1",
    "neg": "function",
    "nop": "function",
    "nosplit": "keyword1",
    "not": "function",
    "o16": "keyword1",
    "o32": "keyword1",
    "offset": "keyword1",
    "opattr": "keyword1",
    "option": "keyword1",
    "or": "function",
    "org": "keyword1",
    "orps": "function",
    "out": "function",
    "outs": "function",
    "outsb": "function",
    "outsd": "function",
    "outsw": "function",
    "overflow?": "keyword1",
    "packssdw": "function",
    "packsswb": "function",
    "packuswb": "function",
    "paddb": "function",
    "paddd": "function",
    "paddsb": "function",
    "paddsw": "function",
    "paddusb": "function",
    "paddusw": "function",
    "paddw": "function",
    "page": "keyword1",
    "pand": "function",
    "pandn": "function",
    "parity?": "keyword1",
    "pavgb": "function",
    "pavgusb": "function",
    "pavgw": "function",
    "pcmpeqb": "function",
    "pcmpeqd": "function",
    "pcmpeqw": "function",
    "pcmpgtb": "function",
    "pcmpgtd": "function",
    "pcmpgtw": "function",
    "pextrw": "function",
    "pf2id": "function",
    "pf2iw": "function",
    "pfacc": "function",
    "pfadd": "function",
    "pfcmpeq": "function",
    "pfcmpge": "function",
    "pfcmpgt": "function",
    "pfmax": "function",
    "pfmin": "function",
    "pfmul": "function",
    "pfnacc": "function",
    "pfpnacc": "function",
    "pfrcp": "function",
    "pfrcpit1": "function",
    "pfrcpit2": "function",
    "pfrsqit1": "function",
    "pfrsqrt": "function",
    "pfsub": "function",
    "pfsubr": "function",
    "pi2fd": "function",
    "pi2fw": "function",
    "pinsrw": "function",
    "pmaddwd": "function",
    "pmaxsw": "function",
    "pmaxub": "function",
    "pminsw": "function",
    "pminub": "function",
    "pmovmskb": "function",
    "pmulhrw": "function",
    "pmulhuw": "function",
    "pmulhw": "function",
    "pmullw": "function",
    "pop": "function",
    "popa": "function",
    "popad": "function",
    "popaw": "function",
    "popcontext": "keyword1",
    "popf": "function",
    "popfd": "function",
    "popfw": "function",
    "por": "function",
    "prefetch": "function",
    "prefetchnta": "function",
    "prefetcht0": "function",
    "prefetcht1": "function",
    "prefetcht2": "function",
    "prefetchw": "function",
    "private": "keyword1",
    "proc": "keyword1",
    "proto": "keyword1",
    "psadbw": "function",
    "pshufw": "function",
    "pslld": "function",
    "psllq": "function",
    "psllw": "function",
    "psrad": "function",
    "psraw": "function",
    "psrld": "function",
    "psrlq": "function",
    "psrlw": "function",
    "psubb": "function",
    "psubd": "function",
    "psubsb": "function",
    "psubsw": "function",
    "psubusb": "function",
    "psubusw": "function",
    "psubw": "function",
    "pswapd": "function",
    "ptr": "keyword1",
    "public": "keyword1",
    "punpckhbw": "function",
    "punpckhdq": "function",
    "punpckhwd": "function",
    "punpcklbw": "function",
    "punpckldq": "function",
    "punpcklwd": "function",
    "purge": "keyword1",
    "push": "function",
    "pusha": "function",
    "pushad": "function",
    "pushaw": "function",
    "pushcontext": "keyword1",
    "pushf": "function",
    "pushfd": "function",
    "pushfw": "function",
    "pxor": "function",
    "qword": "keyword2",
    "rcl": "function",
    "rcr": "function",
    "rdmsr": "function",
    "rdpmc": "function",
    "rdtsc": "function",
    "real10": "keyword2",
    "real4": "keyword2",
    "real8": "keyword2",
    "record": "keyword1",
    "rep": "function",
    "repe": "function",
    "repeat": "keyword1",
    "repne": "function",
    "repnz": "function",
    "rept": "keyword1",
    "repz": "function",
    "resb": "keyword2",
    "resd": "keyword2",
    "resq": "keyword2",
    "rest": "keyword2",
    "resw": "keyword2",
    "ret": "function",
    "retf": "function",
    "retn": "function",
    "rol": "function",
    "ror": "function",
    "rsm": "function",
    "sahf": "function",
    "sal": "function",
    "sar": "function",
    "sbb": "function",
    "sbyte": "keyword2",
    "scas": "function",
    "scasb": "function",
    "scasd": "function",
    "scasw": "function",
    "sdword": "keyword2",
    "section": "keyword1",
    "seg": "keyword1",
    "segment": "keyword1",
    "seta": "function",
    "setae": "function",
    "setb": "function",
    "setbe": "function",
    "setc": "function",
    "sete": "function",
    "setg": "function",
    "setge": "function",
    "setl": "function",
    "setle": "function",
    "setna": "function",
    "setnae": "function",
    "setnb": "function",
    "setnbe": "function",
    "setnc": "function",
    "setne": "function",
    "setng": "function",
    "setnge": "function",
    "setnl": "function",
    "setnle": "function",
    "setno": "function",
    "setnp": "function",
    "setns": "function",
    "setnz": "function",
    "seto": "function",
    "setp": "function",
    "setpe": "function",
    "setpo": "function",
    "sets": "function",
    "setz": "function",
    "sfence": "function",
    "sgdt": "function",
    "shl": "function",
    "shld": "function",
    "short": "keyword1",
    "shr": "function",
    "shrd": "function",
    "shufps": "function",
    "si": "keyword3",
    "sidt": "function",
    "sign?": "keyword1",
    "size": "keyword1",
    "sizeof": "keyword1",
    "sizestr": "keyword1",
    "sldt": "function",
    "smsw": "function",
    "sp": "keyword3",
    "sqrtps": "function",
    "sqrtss": "function",
    "ss": "keyword3",
    "st": "keyword3",
    "st0": "keyword3",
    "st1": "keyword3",
    "st2": "keyword3",
    "st3": "keyword3",
    "st4": "keyword3",
    "st5": "keyword3",
    "st6": "keyword3",
    "st7": "keyword3",
    "stack": "keyword1",
    "stc": "function",
    "std": "function",
    "sti": "function",
    "stmxcsr": "function",
    "stos": "function",
    "stosb": "function",
    "stosd": "function",
    "stosw": "function",
    "str": "function",
    "struc": "keyword1",
    "struct": "keyword1",
    "sub": "function",
    "subps": "function",
    "subss": "function",
    "substr": "keyword1",
    "subtitle": "keyword1",
    "subttl": "keyword1",
    "sword": "keyword2",
    "sysenter": "function",
    "sysexit": "function",
    "tbyte": "keyword2",
    "test": "function",
    "textequ": "keyword2",
    "this": "keyword1",
    "times": "keyword2",
    "title": "keyword1",
    "tr3": "keyword3",
    "tr4": "keyword3",
    "tr5": "keyword3",
    "tr6": "keyword3",
    "tr7": "keyword3",
    "tword": "keyword2",
    "type": "keyword1",
    "typedef": "keyword1",
    "ub2": "function",
    "ucomiss": "function",
    "union": "keyword1",
    "unpckhps": "function",
    "unpcklps": "function",
    "use16": "keyword1",
    "use32": "keyword1",
    "uses": "keyword1",
    "verr": "function",
    "verw": "function",
    "wait": "function",
    "wbinvd": "function",
    "while": "keyword1",
    "word": "keyword2",
    "wrmsr": "function",
    "wrt": "keyword1",
    "xadd": "function",
    "xchg": "function",
    "xlat": "function",
    "xlatb": "function",
    "xmm0": "keyword3",
    "xmm1": "keyword3",
    "xmm2": "keyword3",
    "xmm3": "keyword3",
    "xmm4": "keyword3",
    "xmm5": "keyword3",
    "xmm6": "keyword3",
    "xmm7": "keyword3",
    "xor": "function",
    "xorps": "function",
    "zero?": "keyword1",
}

# Dictionary of keywords dictionaries for assembly_x86 mode.
keywordsDictDict = {
    "assembly_x86_main": assembly_x86_main_keywords_dict,
}

# Rules for assembly_x86_main ruleset.

def assembly_x86_rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def assembly_x86_rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def assembly_x86_rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def assembly_x86_rule3(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="label", pattern="%%",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def assembly_x86_rule4(colorer, s, i):
    return colorer.match_mark_following(s, i, kind="keyword2", pattern="%",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=False)

def assembly_x86_rule5(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def assembly_x86_rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_x86_rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_x86_rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_x86_rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_x86_rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_x86_rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_x86_rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_x86_rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_x86_rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_x86_rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_x86_rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_x86_rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_x86_rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def assembly_x86_rule19(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for assembly_x86_main ruleset.
rulesDict1 = {
    "!": [assembly_x86_rule15,],
    "\"": [assembly_x86_rule2,],
    "%": [assembly_x86_rule3, assembly_x86_rule4, assembly_x86_rule10,],
    "&": [assembly_x86_rule13,],
    "'": [assembly_x86_rule1,],
    "*": [assembly_x86_rule9,],
    "+": [assembly_x86_rule6,],
    "-": [assembly_x86_rule7,],
    ".": [assembly_x86_rule19,],
    "/": [assembly_x86_rule8,],
    "0": [assembly_x86_rule19,],
    "1": [assembly_x86_rule19,],
    "2": [assembly_x86_rule19,],
    "3": [assembly_x86_rule19,],
    "4": [assembly_x86_rule19,],
    "5": [assembly_x86_rule19,],
    "6": [assembly_x86_rule19,],
    "7": [assembly_x86_rule19,],
    "8": [assembly_x86_rule19,],
    "9": [assembly_x86_rule19,],
    ":": [assembly_x86_rule5,],
    ";": [assembly_x86_rule0,],
    "<": [assembly_x86_rule17,],
    "=": [assembly_x86_rule16,],
    ">": [assembly_x86_rule18,],
    "?": [assembly_x86_rule19,],
    "@": [assembly_x86_rule19,],
    "A": [assembly_x86_rule19,],
    "B": [assembly_x86_rule19,],
    "C": [assembly_x86_rule19,],
    "D": [assembly_x86_rule19,],
    "E": [assembly_x86_rule19,],
    "F": [assembly_x86_rule19,],
    "G": [assembly_x86_rule19,],
    "H": [assembly_x86_rule19,],
    "I": [assembly_x86_rule19,],
    "J": [assembly_x86_rule19,],
    "K": [assembly_x86_rule19,],
    "L": [assembly_x86_rule19,],
    "M": [assembly_x86_rule19,],
    "N": [assembly_x86_rule19,],
    "O": [assembly_x86_rule19,],
    "P": [assembly_x86_rule19,],
    "Q": [assembly_x86_rule19,],
    "R": [assembly_x86_rule19,],
    "S": [assembly_x86_rule19,],
    "T": [assembly_x86_rule19,],
    "U": [assembly_x86_rule19,],
    "V": [assembly_x86_rule19,],
    "W": [assembly_x86_rule19,],
    "X": [assembly_x86_rule19,],
    "Y": [assembly_x86_rule19,],
    "Z": [assembly_x86_rule19,],
    "^": [assembly_x86_rule12,],
    "_": [assembly_x86_rule19,],
    "a": [assembly_x86_rule19,],
    "b": [assembly_x86_rule19,],
    "c": [assembly_x86_rule19,],
    "d": [assembly_x86_rule19,],
    "e": [assembly_x86_rule19,],
    "f": [assembly_x86_rule19,],
    "g": [assembly_x86_rule19,],
    "h": [assembly_x86_rule19,],
    "i": [assembly_x86_rule19,],
    "j": [assembly_x86_rule19,],
    "k": [assembly_x86_rule19,],
    "l": [assembly_x86_rule19,],
    "m": [assembly_x86_rule19,],
    "n": [assembly_x86_rule19,],
    "o": [assembly_x86_rule19,],
    "p": [assembly_x86_rule19,],
    "q": [assembly_x86_rule19,],
    "r": [assembly_x86_rule19,],
    "s": [assembly_x86_rule19,],
    "t": [assembly_x86_rule19,],
    "u": [assembly_x86_rule19,],
    "v": [assembly_x86_rule19,],
    "w": [assembly_x86_rule19,],
    "x": [assembly_x86_rule19,],
    "y": [assembly_x86_rule19,],
    "z": [assembly_x86_rule19,],
    "|": [assembly_x86_rule11,],
    "~": [assembly_x86_rule14,],
}

# x.rulesDictDict for assembly_x86 mode.
rulesDictDict = {
    "assembly_x86_main": rulesDict1,
}

# Import dict for assembly_x86 mode.
importDict = {}
