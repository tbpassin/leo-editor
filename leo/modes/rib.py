# Leo colorizer control file for rib mode.
# This file is in the public domain.

# Properties for rib mode.
properties = {
    "doubleBracketIndent": "false",
    "indentNextLines": "Begin|WorldBegin|FrameBegin|TransformBegin|AttributeBegin|SolidBegin|ObjectBegin|MotionBegin",
    "lineComment": "#",
    "lineUpClosingBracket": "true",
}

# Attributes dict for rib_main ruleset.
rib_main_attributes_dict = {
    "default": "null",
    "digit_re": "([[:digit:]]+(e[[:digit:]]*)?)",
    "escape": "\\",
    "highlight_digits": "true",
    "ignore_case": "false",
    "no_word_sep": "",
}

# Attributes dict for rib_literals ruleset.
rib_literals_attributes_dict = {
    "default": "LITERAL1",
    "digit_re": "([[:digit:]]+(e[[:digit:]]*)?)",
    "escape": "\\",
    "highlight_digits": "true",
    "ignore_case": "false",
    "no_word_sep": "",
}

# Dictionary of attributes dictionaries for rib mode.
attributesDictDict = {
    "rib_literals": rib_literals_attributes_dict,
    "rib_main": rib_main_attributes_dict,
}

# Keywords dict for rib_main ruleset.
rib_main_keywords_dict = {
    "ArchiveRecord": "keyword4",
    "AreaLightSource": "keyword2",
    "Atmosphere": "keyword2",
    "Attribute": "keyword2",
    "AttributeBegin": "keyword2",
    "AttributeEnd": "keyword2",
    "Basis": "keyword3",
    "Begin": "keyword2",
    "Blobby": "keyword3",
    "Bound": "keyword2",
    "Clipping": "keyword2",
    "ClippingPlane": "keyword2",
    "Color": "keyword2",
    "ColorSamples": "keyword2",
    "ConcatTransform": "keyword2",
    "Cone": "keyword3",
    "Context": "keyword2",
    "ContextHandle": "keyword2",
    "CoordSysTransform": "keyword2",
    "CoordinateSystem": "keyword2",
    "CropWindow": "keyword2",
    "Curves": "keyword3",
    "Cylinder": "keyword3",
    "Declare": "keyword2",
    "Deformation": "keyword4",
    "DelayedReadArchive": "keyword3",
    "DepthOfField": "keyword2",
    "Detail": "keyword2",
    "DetailRange": "keyword2",
    "Disk": "keyword3",
    "Displacement": "keyword2",
    "Display": "keyword2",
    "DynamicLoad": "keyword3",
    "End": "keyword2",
    "ErrorHandler": "keyword4",
    "Exposure": "keyword2",
    "Exterior": "keyword2",
    "Format": "keyword2",
    "FrameAspectRatio": "keyword2",
    "FrameBegin": "keyword2",
    "FrameEnd": "keyword2",
    "GeneralPolygon": "keyword3",
    "GeometricApproximation": "keyword2",
    "Geometry": "keyword3",
    "Hider": "keyword2",
    "Hyperboloid": "keyword3",
    "Identity": "keyword2",
    "Illuminate": "keyword2",
    "Imager": "keyword2",
    "Interior": "keyword2",
    "LightSource": "keyword2",
    "MakeBump": "keyword4",
    "MakeCubeFaceEnvironment": "keyword4",
    "MakeLatLongEnvironment": "keyword4",
    "MakeShadow": "keyword4",
    "MakeTexture": "keyword4",
    "Matte": "keyword2",
    "MotionBegin": "keyword2",
    "MotionEnd": "keyword2",
    "NuPatch": "keyword3",
    "ObjectBegin": "keyword3",
    "ObjectEnd": "keyword3",
    "ObjectInstance": "keyword3",
    "Opacity": "keyword2",
    "Option": "keyword2",
    "Orientation": "keyword2",
    "Paraboloid": "keyword3",
    "Patch": "keyword3",
    "PatchMesh": "keyword3",
    "Perspective": "keyword2",
    "PixelFilter": "keyword2",
    "PixelSamples": "keyword2",
    "PixelVariance": "keyword2",
    "Points": "keyword3",
    "PointsGeneralPolygons": "keyword3",
    "PointsPolygons": "keyword3",
    "Polygon": "keyword3",
    "Procedural": "keyword3",
    "Projection": "keyword2",
    "Quantize": "keyword2",
    "ReadArchive": "keyword4",
    "RelativeDetail": "keyword2",
    "ReverseOrientation": "keyword2",
    "Rotate": "keyword2",
    "RtContextHandle": "keyword2",
    "RtLightHandle": "keyword2",
    "RtObjectHandle": "keyword3",
    "RunProgram": "keyword3",
    "Scale": "keyword2",
    "ScreenWindow": "keyword2",
    "ShadingInterpolation": "keyword2",
    "ShadingRate": "keyword2",
    "Shutter": "keyword2",
    "Sides": "keyword2",
    "Skew": "keyword2",
    "SolidBegin": "keyword3",
    "SolidEnd": "keyword3",
    "Sphere": "keyword3",
    "SubdivisionMesh": "keyword3",
    "Surface": "keyword2",
    "TextureCoordinates": "keyword2",
    "Torus": "keyword3",
    "Transform": "keyword2",
    "TransformBegin": "keyword2",
    "TransformEnd": "keyword2",
    "TransformPoints": "keyword2",
    "Translate": "keyword2",
    "TrimCurve": "keyword3",
    "WorldBegin": "keyword2",
    "WorldEnd": "keyword2",
    "color": "keyword1",
    "extern": "keyword1",
    "float": "keyword1",
    "matrix": "keyword1",
    "normal": "keyword1",
    "output": "keyword1",
    "point": "keyword1",
    "string": "keyword1",
    "uniform": "keyword1",
    "varying": "keyword1",
    "vector": "keyword1",
    "void": "keyword1",
}

# Keywords dict for rib_literals ruleset.
rib_literals_keywords_dict = {
    "Cs": "literal2",
    "N": "literal2",
    "NDC": "literal2",
    "Os": "literal2",
    "P": "literal2",
    "Pw": "literal2",
    "Pz": "literal2",
    "RI_INFINITY": "literal2",
    "RI_NULL": "literal2",
    "b-spline": "literal2",
    "bezier": "literal2",
    "bicubic": "literal2",
    "bilinear": "literal2",
    "box": "literal2",
    "camera": "literal2",
    "catmull-clark": "literal2",
    "catmull-rom": "literal2",
    "color": "keyword1",
    "constant": "literal2",
    "corner": "literal2",
    "crease": "literal2",
    "extern": "keyword1",
    "float": "keyword1",
    "gaussian": "literal2",
    "hermite": "literal2",
    "hidden": "literal2",
    "hole": "literal2",
    "inside": "literal2",
    "interpolateboundary": "literal2",
    "lh": "literal2",
    "matrix": "keyword1",
    "nonperiodic": "literal2",
    "normal": "keyword1",
    "null": "literal2",
    "object": "literal2",
    "orthographic": "literal2",
    "output": "keyword1",
    "outside": "literal2",
    "periodic": "literal2",
    "perspective": "literal2",
    "point": "keyword1",
    "power": "literal2",
    "raster": "literal2",
    "rh": "literal2",
    "screen": "literal2",
    "sinc": "literal2",
    "smooth": "literal2",
    "string": "keyword1",
    "triangle": "literal2",
    "uniform": "keyword1",
    "varying": "keyword1",
    "vector": "keyword1",
    "void": "keyword1",
    "world": "literal2",
}

# Dictionary of keywords dictionaries for rib mode.
keywordsDictDict = {
    "rib_literals": rib_literals_keywords_dict,
    "rib_main": rib_main_keywords_dict,
}

# Rules for rib_main ruleset.

def rib_rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="#",
        at_line_start=False, at_whitespace_end=True, at_word_start=False,
        delegate="", exclude_match=False)

def rib_rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment2", seq="#",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rib_rule2(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rib_rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rib_rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rib_rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def rib_rule6(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="rib::literals", exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rib_rule7(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for rib_main ruleset.
rulesDict1 = {
    "\"": [rib_rule6,],
    "#": [rib_rule0, rib_rule1,],
    "+": [rib_rule3,],
    "-": [rib_rule2, rib_rule7,],
    "0": [rib_rule7,],
    "1": [rib_rule7,],
    "2": [rib_rule7,],
    "3": [rib_rule7,],
    "4": [rib_rule7,],
    "5": [rib_rule7,],
    "6": [rib_rule7,],
    "7": [rib_rule7,],
    "8": [rib_rule7,],
    "9": [rib_rule7,],
    "@": [rib_rule7,],
    "A": [rib_rule7,],
    "B": [rib_rule7,],
    "C": [rib_rule7,],
    "D": [rib_rule7,],
    "E": [rib_rule7,],
    "F": [rib_rule7,],
    "G": [rib_rule7,],
    "H": [rib_rule7,],
    "I": [rib_rule7,],
    "J": [rib_rule7,],
    "K": [rib_rule7,],
    "L": [rib_rule7,],
    "M": [rib_rule7,],
    "N": [rib_rule7,],
    "O": [rib_rule7,],
    "P": [rib_rule7,],
    "Q": [rib_rule7,],
    "R": [rib_rule7,],
    "S": [rib_rule7,],
    "T": [rib_rule7,],
    "U": [rib_rule7,],
    "V": [rib_rule7,],
    "W": [rib_rule7,],
    "X": [rib_rule7,],
    "Y": [rib_rule7,],
    "Z": [rib_rule7,],
    "[": [rib_rule4,],
    "]": [rib_rule5,],
    "_": [rib_rule7,],
    "a": [rib_rule7,],
    "b": [rib_rule7,],
    "c": [rib_rule7,],
    "d": [rib_rule7,],
    "e": [rib_rule7,],
    "f": [rib_rule7,],
    "g": [rib_rule7,],
    "h": [rib_rule7,],
    "i": [rib_rule7,],
    "j": [rib_rule7,],
    "k": [rib_rule7,],
    "l": [rib_rule7,],
    "m": [rib_rule7,],
    "n": [rib_rule7,],
    "o": [rib_rule7,],
    "p": [rib_rule7,],
    "q": [rib_rule7,],
    "r": [rib_rule7,],
    "s": [rib_rule7,],
    "t": [rib_rule7,],
    "u": [rib_rule7,],
    "v": [rib_rule7,],
    "w": [rib_rule7,],
    "x": [rib_rule7,],
    "y": [rib_rule7,],
    "z": [rib_rule7,],
}

# Rules for rib_literals ruleset.

def rib_rule8(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for rib_literals ruleset.
rulesDict2 = {
    "-": [rib_rule8,],
    "0": [rib_rule8,],
    "1": [rib_rule8,],
    "2": [rib_rule8,],
    "3": [rib_rule8,],
    "4": [rib_rule8,],
    "5": [rib_rule8,],
    "6": [rib_rule8,],
    "7": [rib_rule8,],
    "8": [rib_rule8,],
    "9": [rib_rule8,],
    "@": [rib_rule8,],
    "A": [rib_rule8,],
    "B": [rib_rule8,],
    "C": [rib_rule8,],
    "D": [rib_rule8,],
    "E": [rib_rule8,],
    "F": [rib_rule8,],
    "G": [rib_rule8,],
    "H": [rib_rule8,],
    "I": [rib_rule8,],
    "J": [rib_rule8,],
    "K": [rib_rule8,],
    "L": [rib_rule8,],
    "M": [rib_rule8,],
    "N": [rib_rule8,],
    "O": [rib_rule8,],
    "P": [rib_rule8,],
    "Q": [rib_rule8,],
    "R": [rib_rule8,],
    "S": [rib_rule8,],
    "T": [rib_rule8,],
    "U": [rib_rule8,],
    "V": [rib_rule8,],
    "W": [rib_rule8,],
    "X": [rib_rule8,],
    "Y": [rib_rule8,],
    "Z": [rib_rule8,],
    "_": [rib_rule8,],
    "a": [rib_rule8,],
    "b": [rib_rule8,],
    "c": [rib_rule8,],
    "d": [rib_rule8,],
    "e": [rib_rule8,],
    "f": [rib_rule8,],
    "g": [rib_rule8,],
    "h": [rib_rule8,],
    "i": [rib_rule8,],
    "j": [rib_rule8,],
    "k": [rib_rule8,],
    "l": [rib_rule8,],
    "m": [rib_rule8,],
    "n": [rib_rule8,],
    "o": [rib_rule8,],
    "p": [rib_rule8,],
    "q": [rib_rule8,],
    "r": [rib_rule8,],
    "s": [rib_rule8,],
    "t": [rib_rule8,],
    "u": [rib_rule8,],
    "v": [rib_rule8,],
    "w": [rib_rule8,],
    "x": [rib_rule8,],
    "y": [rib_rule8,],
    "z": [rib_rule8,],
}

# x.rulesDictDict for rib mode.
rulesDictDict = {
    "rib_literals": rulesDict2,
    "rib_main": rulesDict1,
}

# Import dict for rib mode.
importDict = {}
