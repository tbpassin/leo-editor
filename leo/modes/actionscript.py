# Leo colorizer control file for actionscript mode.
# This file is in the public domain.

# Properties for actionscript mode.
properties = {
    "commentEnd": "*/",
    "commentStart": "/*",
    "doubleBracketIndent": "false",
    "indentCloseBrackets": "}",
    "indentOpenBrackets": "{",
    "indentPrevLine": "\\s*(if|while)\\s*(|else|case|default:)[^;]*|for\\s*\\(.*)",
    "lineComment": "//",
    "lineUpClosingBracket": "true",
    "wordBreakChars": ",+-=<>/?^&*",
}

# Attributes dict for actionscript_main ruleset.
actionscript_main_attributes_dict = {
    "default": "null",
    "digit_re": "",
    "escape": "\\",
    "highlight_digits": "true",
    "ignore_case": "false",
    "no_word_sep": "",
}

# Dictionary of attributes dictionaries for actionscript mode.
attributesDictDict = {
    "actionscript_main": actionscript_main_attributes_dict,
}

# Keywords dict for actionscript_main ruleset.
actionscript_main_keywords_dict = {
    "#endinitclip": "keyword1",
    "#include": "literal2",
    "#initclip": "keyword1",
    "ASSetPropFlags": "literal2",
    "Accessibility": "literal2",
    "Array": "keyword3",
    "BACKSPACE": "literal2",
    "Boolean": "literal2",
    "CAPSLOCK": "literal2",
    "CONTROL": "literal2",
    "Camera": "literal2",
    "Color": "keyword3",
    "ContextMenu": "literal2",
    "ContextMenuItem": "literal2",
    "CustomActions": "literal2",
    "DELETEKEY": "literal2",
    "DOWN": "literal2",
    "DataGlue": "literal2",
    "Date": "literal2",
    "E": "literal2",
    "END": "literal2",
    "ENTER": "literal2",
    "ESCAPE": "literal2",
    "Error": "literal2",
    "Function": "keyword3",
    "HOME": "literal2",
    "INSERT": "literal2",
    "Infinity": "literal2",
    "Key": "keyword3",
    "LEFT": "literal2",
    "LN10": "literal2",
    "LN2": "literal2",
    "LOG10E": "literal2",
    "LOG2E": "literal2",
    "LoadVars": "literal2",
    "LocalConnection": "literal2",
    "MAX_VALUE": "literal2",
    "MIN_VALUE": "literal2",
    "MMExecute": "keyword3",
    "Math": "keyword3",
    "Microphone": "literal2",
    "Mouse": "keyword3",
    "MovieClip": "keyword3",
    "MovieClipLoader": "literal2",
    "NEGATIVE_INFINITY": "literal2",
    "NaN": "literal2",
    "NetConnection": "literal2",
    "NetServices": "literal2",
    "NetStream": "literal2",
    "Number": "literal2",
    "Object": "keyword3",
    "PGDN": "literal2",
    "PGUP": "literal2",
    "PI": "literal2",
    "POSITIVE_INFINITY": "literal2",
    "PrintJob": "literal2",
    "RIGHT": "literal2",
    "SHIFT": "literal2",
    "SPACE": "literal2",
    "SQRT1_2": "literal2",
    "SQRT2": "literal2",
    "Selection": "keyword3",
    "SharedObject": "literal2",
    "Sound": "keyword3",
    "Stage": "literal2",
    "String": "literal2",
    "StyleSheet": "literal2",
    "System": "literal2",
    "TAB": "literal2",
    "TextField": "literal2",
    "TextFormat": "literal2",
    "TextSnapshot": "literal2",
    "UP": "literal2",
    "UTC": "literal2",
    "Video": "literal2",
    "Void": "keyword1",
    "XML": "keyword3",
    "XMLNode": "keyword3",
    "XMLSocket": "keyword3",
    "__constructor__": "literal2",
    "__proto__": "literal2",
    "_accProps": "literal2",
    "_alpha": "literal2",
    "_currentframe": "literal2",
    "_droptarget": "literal2",
    "_focusrect": "literal2",
    "_framesloaded": "literal2",
    "_global": "literal2",
    "_height": "literal2",
    "_highquality": "keyword2",
    "_level": "literal2",
    "_lockroot": "literal2",
    "_name": "literal2",
    "_parent": "literal2",
    "_quality": "literal2",
    "_root": "literal2",
    "_rotation": "literal2",
    "_soundbuftime": "literal2",
    "_target": "literal2",
    "_totalframes": "literal2",
    "_url": "literal2",
    "_visible": "literal2",
    "_width": "literal2",
    "_x": "literal2",
    "_xmouse": "literal2",
    "_xscale": "literal2",
    "_y": "literal2",
    "_ymouse": "literal2",
    "_yscale": "literal2",
    "abs": "literal2",
    "abstract": "keyword1",
    "acos": "literal2",
    "activityLevel": "literal2",
    "add": "keyword1",
    "addItem": "literal2",
    "addItemAt": "literal2",
    "addListener": "literal2",
    "addPage": "literal2",
    "addProperty": "literal2",
    "addRequestHeader": "literal2",
    "addView": "literal2",
    "align": "literal2",
    "allowDomain": "literal2",
    "allowInsecureDomain": "literal2",
    "and": "keyword1",
    "appendChild": "literal2",
    "apply": "literal2",
    "arguments": "literal2",
    "asin": "literal2",
    "atan": "literal2",
    "atan2": "literal2",
    "attachAudio": "literal2",
    "attachMovie": "literal2",
    "attachSound": "literal2",
    "attributes": "literal2",
    "autoSize": "literal2",
    "avHardwareDisable": "literal2",
    "background": "literal2",
    "backgroundColor": "literal2",
    "bandwidth": "literal2",
    "beginFill": "literal2",
    "beginGradientFill": "literal2",
    "bindFormatFunction": "literal2",
    "bindFormatStrings": "literal2",
    "blockIndent": "literal2",
    "bold": "literal2",
    "boolean": "keyword3",
    "border": "literal2",
    "borderColor": "literal2",
    "bottomScroll": "literal2",
    "break": "keyword1",
    "bufferLength": "literal2",
    "bufferTime": "literal2",
    "builtInItems": "literal2",
    "bullet": "literal2",
    "byte": "keyword3",
    "bytesLoaded": "literal2",
    "bytesTotal": "literal2",
    "call": "literal2",
    "callee": "literal2",
    "caller": "literal2",
    "capabilities": "literal2",
    "caption": "literal2",
    "case": "keyword1",
    "catch": "keyword1",
    "ceil": "literal2",
    "char": "keyword3",
    "charAt": "literal2",
    "charCodeAt": "literal2",
    "childNodes": "literal2",
    "chr": "keyword2",
    "class": "keyword1",
    "clear": "literal2",
    "clearInterval": "literal2",
    "cloneNode": "literal2",
    "close": "literal2",
    "color": "literal2",
    "concat": "literal2",
    "connect": "literal2",
    "const": "keyword1",
    "contentType": "literal2",
    "continue": "keyword1",
    "copy": "literal2",
    "cos": "literal2",
    "createElement": "literal2",
    "createEmptyMovieClip": "literal2",
    "createGatewayConnection": "literal2",
    "createTextField": "literal2",
    "createTextNode": "literal2",
    "currentFps": "literal2",
    "curveTo": "literal2",
    "customItems": "literal2",
    "data": "literal2",
    "deblocking": "literal2",
    "debugger": "keyword1",
    "default": "keyword1",
    "delete": "keyword1",
    "do": "keyword1",
    "docTypeDecl": "literal2",
    "domain": "literal2",
    "double": "keyword3",
    "duplicateMovieClip": "literal2",
    "duration": "literal2",
    "dynamic": "keyword1",
    "else": "keyword1",
    "embedFonts": "literal2",
    "enabled": "literal2",
    "endFill": "literal2",
    "enum": "keyword1",
    "eq": "keyword1",
    "escape": "literal2",
    "eval": "literal2",
    "exactSettings": "literal2",
    "exp": "literal2",
    "export": "keyword2",
    "extends": "keyword1",
    "false": "literal2",
    "filter": "literal2",
    "final": "keyword1",
    "finally": "keyword1",
    "findText": "literal2",
    "firstChild": "literal2",
    "float": "keyword3",
    "floor": "literal2",
    "flush": "literal2",
    "focusEnabled": "literal2",
    "font": "literal2",
    "for": "keyword1",
    "fps": "literal2",
    "fromCharCode": "literal2",
    "fscommand": "literal2",
    "function": "keyword1",
    "gain": "literal2",
    "ge": "keyword1",
    "get": "literal2",
    "getAscii": "literal2",
    "getBeginIndex": "literal2",
    "getBounds": "literal2",
    "getBytesLoaded": "literal2",
    "getBytesTotal": "literal2",
    "getCaretIndex": "literal2",
    "getCode": "literal2",
    "getColumnNames": "literal2",
    "getCount": "literal2",
    "getDate": "literal2",
    "getDay": "literal2",
    "getDebug": "literal2",
    "getDebugConfig": "literal2",
    "getDebugID": "literal2",
    "getDepth": "literal2",
    "getEndIndex": "literal2",
    "getFocus": "literal2",
    "getFontList": "literal2",
    "getFullYear": "literal2",
    "getHours": "literal2",
    "getInstanceAtDepth": "literal2",
    "getItemAt": "literal2",
    "getLength": "literal2",
    "getLocal": "literal2",
    "getMilliseconds": "literal2",
    "getMinutes": "literal2",
    "getMonth": "literal2",
    "getNewTextFormat": "literal2",
    "getNextHighestDepth": "literal2",
    "getNumberAvailable": "literal2",
    "getPan": "literal2",
    "getProgress": "literal2",
    "getProperty": "literal2",
    "getRGB": "literal2",
    "getSWFVersion": "literal2",
    "getSeconds": "literal2",
    "getSelected": "literal2",
    "getSelectedText": "literal2",
    "getService": "literal2",
    "getSize": "literal2",
    "getStyle": "literal2",
    "getStyleNames": "literal2",
    "getText": "literal2",
    "getTextExtent": "literal2",
    "getTextFormat": "literal2",
    "getTextSnapshot": "literal2",
    "getTime": "literal2",
    "getTimer": "literal2",
    "getTimezoneOffset": "literal2",
    "getTransform": "literal2",
    "getURL": "literal2",
    "getUTCDate": "literal2",
    "getUTCDay": "literal2",
    "getUTCFullYear": "literal2",
    "getUTCHours": "literal2",
    "getUTCMilliseconds": "literal2",
    "getUTCMinutes": "literal2",
    "getUTCMonth": "literal2",
    "getUTCSeconds": "literal2",
    "getVersion": "literal2",
    "getVolume": "literal2",
    "getYear": "literal2",
    "globalToLocal": "literal2",
    "goto": "keyword1",
    "gotoAndPlay": "literal2",
    "gotoAndStop": "literal2",
    "gt": "keyword1",
    "hasAccessibility": "literal2",
    "hasAudio": "literal2",
    "hasAudioEncoder": "literal2",
    "hasChildNodes": "literal2",
    "hasEmbeddedVideo": "literal2",
    "hasMP3": "literal2",
    "hasPrinting": "literal2",
    "hasScreenBroadcast": "literal2",
    "hasScreenPlayback": "literal2",
    "hasStreamingAudio": "literal2",
    "hasStreamingVideo": "literal2",
    "hasVideoEncoder": "literal2",
    "height": "literal2",
    "hide": "literal2",
    "hideBuiltInItems": "literal2",
    "hitArea": "literal2",
    "hitTest": "literal2",
    "hitTestTextNearPos": "literal2",
    "hscroll": "literal2",
    "html": "literal2",
    "htmlText": "literal2",
    "id3": "literal2",
    "if": "keyword1",
    "ifFrameLoaded": "keyword1",
    "ignoreWhite": "literal2",
    "implements": "keyword1",
    "import": "keyword2",
    "in": "keyword1",
    "indent": "literal2",
    "index": "literal2",
    "indexOf": "literal2",
    "insertBefore": "literal2",
    "install": "literal2",
    "instanceof": "keyword1",
    "int": "keyword3",
    "interface": "keyword1",
    "isActive": "literal2",
    "isDebugger": "literal2",
    "isDown": "literal2",
    "isFinite": "literal2",
    "isFullyPopulated": "literal2",
    "isLocal": "literal2",
    "isNaN": "literal2",
    "isToggled": "literal2",
    "italic": "literal2",
    "join": "literal2",
    "language": "literal2",
    "lastChild": "literal2",
    "lastIndexOf": "literal2",
    "le": "keyword1",
    "leading": "literal2",
    "leftMargin": "literal2",
    "length": "literal2",
    "lineStyle": "literal2",
    "lineTo": "literal2",
    "list": "literal2",
    "load": "literal2",
    "loadClip": "literal2",
    "loadMovie": "literal2",
    "loadMovieNum": "literal2",
    "loadSound": "literal2",
    "loadVariables": "literal2",
    "loadVariablesNum": "literal2",
    "loaded": "literal2",
    "localFileReadDisable": "literal2",
    "localToGlobal": "literal2",
    "log": "literal2",
    "long": "keyword3",
    "lt": "keyword1",
    "manufacturer": "literal2",
    "max": "literal2",
    "maxChars": "literal2",
    "maxhscroll": "literal2",
    "maxscroll": "literal2",
    "mbchr": "keyword2",
    "mblength": "keyword2",
    "mbord": "keyword2",
    "mbsubstring": "keyword2",
    "menu": "literal2",
    "message": "literal2",
    "min": "literal2",
    "motionLevel": "literal2",
    "motionTimeOut": "literal2",
    "mouseWheelEnabled": "literal2",
    "moveTo": "literal2",
    "multiline": "literal2",
    "muted": "literal2",
    "name": "literal2",
    "names": "literal2",
    "native": "keyword1",
    "ne": "keyword1",
    "new": "keyword1",
    "newline": "literal2",
    "nextFrame": "literal2",
    "nextScene": "literal2",
    "nextSibling": "literal2",
    "nodeName": "literal2",
    "nodeType": "literal2",
    "nodeValue": "literal2",
    "not": "keyword1",
    "null": "literal2",
    "on": "keyword1",
    "onActivity": "literal2",
    "onChanged": "literal2",
    "onClipEvent": "keyword1",
    "onClose": "literal2",
    "onConnect": "literal2",
    "onData": "literal2",
    "onDragOut": "literal2",
    "onDragOver": "literal2",
    "onEnterFrame": "literal2",
    "onID3": "literal2",
    "onKeyDown": "literal2",
    "onKeyUp": "literal2",
    "onKillFocus": "literal2",
    "onLoad": "literal2",
    "onLoadComplete": "literal2",
    "onLoadError": "literal2",
    "onLoadInit": "literal2",
    "onLoadProgress": "literal2",
    "onLoadStart": "literal2",
    "onMouseDown": "literal2",
    "onMouseMove": "literal2",
    "onMouseUp": "literal2",
    "onMouseWheel": "literal2",
    "onPress": "literal2",
    "onRelease": "literal2",
    "onReleaseOutside": "literal2",
    "onResize": "literal2",
    "onRollOut": "literal2",
    "onRollOver": "literal2",
    "onScroller": "literal2",
    "onSelect": "literal2",
    "onSetFocus": "literal2",
    "onSoundComplete": "literal2",
    "onStatus": "literal2",
    "onUnload": "literal2",
    "onUpdate": "literal2",
    "onXML": "literal2",
    "or": "keyword1",
    "ord": "keyword2",
    "os": "literal2",
    "package": "keyword2",
    "parentNode": "literal2",
    "parseCSS": "literal2",
    "parseFloat": "literal2",
    "parseInt": "literal2",
    "parseXML": "literal2",
    "password": "literal2",
    "pause": "literal2",
    "pixelAspectRatio": "literal2",
    "play": "literal2",
    "playerType": "literal2",
    "pop": "literal2",
    "position": "literal2",
    "pow": "literal2",
    "prevFrame": "literal2",
    "prevScene": "literal2",
    "previousSibling": "literal2",
    "print": "literal2",
    "printAsBitmap": "literal2",
    "printAsBitmapNum": "literal2",
    "printNum": "literal2",
    "private": "keyword1",
    "protected": "keyword1",
    "prototype": "literal2",
    "public": "keyword1",
    "push": "literal2",
    "quality": "literal2",
    "random": "literal2",
    "rate": "literal2",
    "registerClass": "literal2",
    "removeAll": "literal2",
    "removeItemAt": "literal2",
    "removeListener": "literal2",
    "removeMovieClip": "literal2",
    "removeNode": "literal2",
    "removeTextField": "literal2",
    "replaceItemAt": "literal2",
    "replaceSel": "literal2",
    "replaceText": "literal2",
    "restrict": "literal2",
    "return": "keyword1",
    "reverse": "literal2",
    "rightMargin": "literal2",
    "round": "literal2",
    "scaleMode": "literal2",
    "screenColor": "literal2",
    "screenDPI": "literal2",
    "screenResolutionX": "literal2",
    "screenResolutionY": "literal2",
    "scroll": "literal2",
    "security": "literal2",
    "seek": "literal2",
    "selectable": "literal2",
    "send": "literal2",
    "sendAndLoad": "literal2",
    "separatorBefore": "literal2",
    "serverString": "literal2",
    "setBufferTime": "literal2",
    "setClipboard": "literal2",
    "setCredentials": "literal2",
    "setDate": "literal2",
    "setDebug": "literal2",
    "setDebugID": "literal2",
    "setDefaultGatewayURL": "literal2",
    "setDeliveryMode": "literal2",
    "setField": "literal2",
    "setFocus": "literal2",
    "setFullYear": "literal2",
    "setGain": "literal2",
    "setHours": "literal2",
    "setI": "literal2",
    "setInterval": "literal2",
    "setMask": "literal2",
    "setMilliseconds": "literal2",
    "setMinutes": "literal2",
    "setMode": "literal2",
    "setMonth": "literal2",
    "setMotionLevel": "literal2",
    "setNewTextFormat": "literal2",
    "setPan": "literal2",
    "setProperty": "literal2",
    "setQuality": "literal2",
    "setRGB": "literal2",
    "setRate": "literal2",
    "setSeconds": "literal2",
    "setSelectColor": "literal2",
    "setSelected": "literal2",
    "setSelection": "literal2",
    "setSilenceLevel": "literal2",
    "setStyle": "literal2",
    "setTextFormat": "literal2",
    "setTime": "literal2",
    "setTransform": "literal2",
    "setUTCDate": "literal2",
    "setUTCFullYear": "literal2",
    "setUTCHours": "literal2",
    "setUTCMilliseconds": "literal2",
    "setUTCMinutes": "literal2",
    "setUTCMonth": "literal2",
    "setUTCSeconds": "literal2",
    "setUseEchoSuppression": "literal2",
    "setVolume": "literal2",
    "setYear": "literal2",
    "shift": "literal2",
    "short": "keyword3",
    "show": "literal2",
    "showMenu": "literal2",
    "showSettings": "literal2",
    "silenceLevel": "literal2",
    "silenceTimeout": "literal2",
    "sin": "literal2",
    "size": "literal2",
    "slice": "literal2",
    "smoothing": "literal2",
    "sort": "literal2",
    "sortItemsBy": "literal2",
    "sortOn": "literal2",
    "splice": "literal2",
    "split": "literal2",
    "sqrt": "literal2",
    "start": "literal2",
    "startDrag": "literal2",
    "static": "keyword1",
    "status": "literal2",
    "stop": "literal2",
    "stopAllSounds": "literal2",
    "stopDrag": "literal2",
    "styleSheet": "literal2",
    "substr": "literal2",
    "substring": "literal2",
    "super": "literal2",
    "swapDepths": "literal2",
    "switch": "keyword1",
    "synchronized": "keyword1",
    "tabChildren": "literal2",
    "tabEnabled": "literal2",
    "tabIndex": "literal2",
    "tabStops": "literal2",
    "tan": "literal2",
    "target": "literal2",
    "targetPath": "literal2",
    "tellTarget": "literal2",
    "text": "literal2",
    "textColor": "literal2",
    "textHeight": "literal2",
    "textWidth": "literal2",
    "this": "literal2",
    "throw": "keyword1",
    "throws": "keyword1",
    "time": "literal2",
    "toLowerCase": "literal2",
    "toString": "literal2",
    "toUpperCase": "literal2",
    "toggleHighQuality": "literal2",
    "trace": "literal2",
    "trackAsMenu": "literal2",
    "transient": "keyword1",
    "true": "literal2",
    "try": "keyword1",
    "type": "literal2",
    "typeof": "keyword1",
    "undefined": "literal2",
    "underline": "literal2",
    "unescape": "literal2",
    "uninstall": "literal2",
    "unloadClip": "literal2",
    "unloadMovie": "literal2",
    "unloadMovieNum": "literal2",
    "unshift": "literal2",
    "unwatch": "literal2",
    "updateAfterEvent": "literal2",
    "updateProperties": "literal2",
    "url": "literal2",
    "useCodepage": "literal2",
    "useEchoSuppression": "literal2",
    "useHandCursor": "literal2",
    "valueOf": "literal2",
    "var": "keyword1",
    "variable": "literal2",
    "version": "literal2",
    "visible": "literal2",
    "void": "keyword3",
    "volatile": "keyword1",
    "watch": "literal2",
    "while": "keyword1",
    "width": "literal2",
    "with": "keyword1",
    "wordWrap": "literal2",
    "xmlDecl": "literal2",
}

# Dictionary of keywords dictionaries for actionscript mode.
keywordsDictDict = {
    "actionscript_main": actionscript_main_keywords_dict,
}

# Rules for actionscript_main ruleset.

def actionscript_rule0(colorer, s, i):
    return colorer.match_span(s, i, kind="comment1", begin="/*", end="*/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False,
        no_escape=False, no_line_break=False, no_word_break=False)

def actionscript_rule1(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="\"", end="\"",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def actionscript_rule2(colorer, s, i):
    return colorer.match_span(s, i, kind="literal1", begin="'", end="'",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

# Used to color "("
def actionscript_rule3(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="function", pattern="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def actionscript_rule4(colorer, s, i):
    return colorer.match_eol_span(s, i, kind="comment1", seq="//",
        at_line_start=False, at_whitespace_end=False, at_word_start=False,
        delegate="", exclude_match=False)

# Used to color ")".  2011/05/22: change kind to "operator". Also changed actionscript.xml.
def actionscript_rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=")",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

# Used to color "(".  2011/05/22: change kind to "operator". Also changed actionscript.xml.
def actionscript_rule6(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="(",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule7(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule8(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="!",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule9(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule10(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<=",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule11(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule12(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule13(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="/",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule14(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="*",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule15(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=">",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule16(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="<",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule17(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="%",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule18(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="&",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule19(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="|",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule20(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="^",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule21(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="~",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule22(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=".",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule23(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="}",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule24(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="{",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule25(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=",",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule26(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=";",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule27(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule28(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule29(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="?",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule30(colorer, s, i):
    return colorer.match_mark_previous(s, i, kind="label", pattern=":",
        at_line_start=True, at_whitespace_end=False, at_word_start=False, exclude_match=True)

def actionscript_rule31(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq=":",
        at_line_start=False, at_whitespace_end=False, at_word_start=False, delegate="")

def actionscript_rule32(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules dict for actionscript_main ruleset.
rulesDict1 = {
    "!": [actionscript_rule8,],
    "\"": [actionscript_rule1,],
    "#": [actionscript_rule32,],
    "%": [actionscript_rule17,],
    "&": [actionscript_rule18,],
    "'": [actionscript_rule2,],
    "(": [actionscript_rule3, actionscript_rule6,],
    ")": [actionscript_rule5,],
    "*": [actionscript_rule14,],
    "+": [actionscript_rule11,],
    ",": [actionscript_rule25,],
    "-": [actionscript_rule12,],
    ".": [actionscript_rule22,],
    "/": [actionscript_rule0, actionscript_rule4, actionscript_rule13,],
    "0": [actionscript_rule32,],
    "1": [actionscript_rule32,],
    "2": [actionscript_rule32,],
    "3": [actionscript_rule32,],
    "4": [actionscript_rule32,],
    "5": [actionscript_rule32,],
    "6": [actionscript_rule32,],
    "7": [actionscript_rule32,],
    "8": [actionscript_rule32,],
    "9": [actionscript_rule32,],
    ":": [actionscript_rule30, actionscript_rule31,],
    ";": [actionscript_rule26,],
    "<": [actionscript_rule10, actionscript_rule16,],
    "=": [actionscript_rule7,],
    ">": [actionscript_rule9, actionscript_rule15,],
    "?": [actionscript_rule29,],
    "@": [actionscript_rule32,],
    "A": [actionscript_rule32,],
    "B": [actionscript_rule32,],
    "C": [actionscript_rule32,],
    "D": [actionscript_rule32,],
    "E": [actionscript_rule32,],
    "F": [actionscript_rule32,],
    "G": [actionscript_rule32,],
    "H": [actionscript_rule32,],
    "I": [actionscript_rule32,],
    "J": [actionscript_rule32,],
    "K": [actionscript_rule32,],
    "L": [actionscript_rule32,],
    "M": [actionscript_rule32,],
    "N": [actionscript_rule32,],
    "O": [actionscript_rule32,],
    "P": [actionscript_rule32,],
    "Q": [actionscript_rule32,],
    "R": [actionscript_rule32,],
    "S": [actionscript_rule32,],
    "T": [actionscript_rule32,],
    "U": [actionscript_rule32,],
    "V": [actionscript_rule32,],
    "W": [actionscript_rule32,],
    "X": [actionscript_rule32,],
    "Y": [actionscript_rule32,],
    "Z": [actionscript_rule32,],
    "[": [actionscript_rule28,],
    "]": [actionscript_rule27,],
    "^": [actionscript_rule20,],
    "_": [actionscript_rule32,],
    "a": [actionscript_rule32,],
    "b": [actionscript_rule32,],
    "c": [actionscript_rule32,],
    "d": [actionscript_rule32,],
    "e": [actionscript_rule32,],
    "f": [actionscript_rule32,],
    "g": [actionscript_rule32,],
    "h": [actionscript_rule32,],
    "i": [actionscript_rule32,],
    "j": [actionscript_rule32,],
    "k": [actionscript_rule32,],
    "l": [actionscript_rule32,],
    "m": [actionscript_rule32,],
    "n": [actionscript_rule32,],
    "o": [actionscript_rule32,],
    "p": [actionscript_rule32,],
    "q": [actionscript_rule32,],
    "r": [actionscript_rule32,],
    "s": [actionscript_rule32,],
    "t": [actionscript_rule32,],
    "u": [actionscript_rule32,],
    "v": [actionscript_rule32,],
    "w": [actionscript_rule32,],
    "x": [actionscript_rule32,],
    "y": [actionscript_rule32,],
    "z": [actionscript_rule32,],
    "{": [actionscript_rule24,],
    "|": [actionscript_rule19,],
    "}": [actionscript_rule23,],
    "~": [actionscript_rule21,],
}

# x.rulesDictDict for actionscript mode.
rulesDictDict = {
    "actionscript_main": rulesDict1,
}

# Import dict for actionscript mode.
importDict = {}
