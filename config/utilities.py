from kmk.keys import KC

def HT(tap, hold):
    return KC.HT(tap, hold, prefer_hold=True, tap_interrupted=False, tap_time=300)

def convert(keyList):
    keyDefinition = {
        "(":KC.LSFT(KC.N8),
        ")":KC.LSFT(KC.N9),
        "[":KC.LSFT(KC.QUOT),
        "]":KC.LSFT(KC.BSLS),
        "{":KC.QUOT,
        "}":KC.BSLS,
        "'":KC.MINS,
        '"':KC.LSFT(KC.N2),
        "`":KC.RALT(KC.BSLS),
        "<":KC.NUBS,
        ">":KC.LSFT(KC.NUBS),
        "/":KC.LSFT(KC.N7),
       "\\":KC.RALT(KC.MINS),
        "¿":KC.EQL,
        "?":KC.LSFT(KC.MINS),
        ".":KC.DOT,
        ",":KC.COMM,
        ":":KC.LSFT(KC.DOT),
        ";":KC.LSFT(KC.COMM),
        "*":KC.LSFT(KC.RBRC),
        "/":KC.LSFT(KC.N7),
        "+":KC.RBRC,
        "-":KC.SLSH,
        "_":KC.LSFT(KC.SLSH),
        "=":KC.LSFT(KC.N0),
        "^":KC.RALT(KC.QUOT),
        "|":KC.GRAVE,
        "!":KC.LSFT(KC.N1),
        "¡":KC.LSFT(KC.EQL),
        "#":KC.LSFT(KC.N3),
        "$":KC.LSFT(KC.N4),
        "%":KC.LSFT(KC.N5),
        "&":KC.LSFT(KC.N6),
        "~":KC.RALT(KC.SCLN),
    }
    newKeys = []
    
    for key in keyList:
        if type(key) == str:
            newKeys.append(keyDefinition.get(key, KC.NO))
        else:
            newKeys.append(key)
    return newKeys
