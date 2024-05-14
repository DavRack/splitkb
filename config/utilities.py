from kmk.keys import KC
from kmk.handlers.sequences import send_string
from boards import getBoard


class Layer:
    layout = []
    id = 0

    def __init__(self, id, profile="linux"):
        self.layout = [KC.NO for _ in range(id)]
        self.id = id
        self.DF = KC.DF(id)
        self.MO = KC.MO(id)
        # this keycodes needs a partial apply to work
        # self.LM = KC.LM(id, mod)
        # self.LT = KC.LT(id, kc)
        self.TG = KC.TG(id)
        self.TO = KC.TO(id)
        self.TT = KC.TT(id)
        self.profile = profile

    def set_layout(self, layout):
        self.layout = convert(layout, profile=self.profile)


class LayerCreator:
    layers = []
    next_layer_id = 0
    profile = "linux"

    def __init__(self, profile="linux") -> None:
        self.kb = getBoard()
        self.layout_lenght = len(self.kb.coord_mapping)
        self.profile = profile

    def create_layer(self):
        new_layer = Layer(self.next_layer_id, self.profile)
        self.layers.append(new_layer)
        self.next_layer_id += 1

        return new_layer

    def get_layers(self):
        return [layer.layout for layer in self.layers]


def HT(tap, hold):
    return KC.HT(convert([tap])[0], convert([hold])[0], prefer_hold=True, tap_interrupted=False, tap_time=300)


def convert(keyList, profile="osx"):
    keyDefinition = {  # default key definition
        "(": KC.LSFT(KC.N8),
        ")": KC.LSFT(KC.N9),
        "[": KC.LSFT(KC.QUOT),
        "]": KC.LSFT(KC.BSLS),
        "{": KC.QUOT,
        "}": KC.BSLS,
        "'": KC.MINS,
        '"': KC.LSFT(KC.N2),
        "<": KC.RO,
        ">": KC.LSFT(KC.RO),
        "/": KC.LSFT(KC.N7),
        "\\": KC.RALT(KC.MINS),
        "¿": KC.EQL,
        "?": KC.LSFT(KC.MINS),
        ".": KC.DOT,
        ",": KC.COMM,
        ":": KC.LSFT(KC.DOT),
        ";": KC.LSFT(KC.COMM),
        "*": KC.LSFT(KC.RBRC),
        "+": KC.RBRC,
        "-": KC.SLSH,
        "_": KC.LSFT(KC.SLSH),
        "=": KC.LSFT(KC.N0),
        "^": KC.RALT(KC.QUOT),
        "|": KC.NUBS,
        "!": KC.LSFT(KC.N1),
        "¡": KC.LSFT(KC.EQL),
        "#": KC.LSFT(KC.N3),
        "$": KC.LSFT(KC.N4),
        "%": KC.LSFT(KC.N5),
        "&": KC.LSFT(KC.N6),
        "~": KC.RALT(KC.SCLN),
        "@": KC.RALT(KC.Q),
        "´": KC.LBRC,
        "`": KC.RALT(KC.BSLS),
    }

    if profile == "osx":
        keyDefinition["`"] = KC.RALT(KC.BSLS)

    newKeys = []

    for key in keyList:
        if type(key) == str:
            k = keyDefinition.get(key, KC.NO)
            newKeys.append(k)
        else:
            newKeys.append(key)
    return newKeys
