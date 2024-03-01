from kmk.keys import KC
from boards import getBoard

class Layer:
    layout = []
    id = 0

    def __init__(self, id):
        self.layout = [ KC.NO for _ in range(id)]
        self.id = id
        self.DF = KC.DF(id)
        self.MO = KC.MO(id)
        # this keycodes needs a partial apply to work
        # self.LM = KC.LM(id, mod) 
        # self.LT = KC.LT(id, kc)
        self.TG = KC.TG(id)
        self.TO = KC.TO(id)
        self.TT = KC.TT(id)

    def set_layout(self, layout):
        self.layout = convert(layout)

class LayerCreator:
    layers = []
    next_layer_id = 0

    def __init__(self) -> None:
        self.kb = getBoard()
        self.layout_lenght = len(self.kb.coord_mapping)
    
    def create_layer(self):
        new_layer = Layer(self.next_layer_id)
        self.layers.append(new_layer)
        self.next_layer_id += 1

        return new_layer
    
    def get_layers(self):
        return [layer.layout for layer in self.layers]



def HT(tap, hold):
    return KC.HT(convert([tap])[0], convert([hold])[0], prefer_hold=True, tap_interrupted=False, tap_time=300)

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
        "@":KC.RALT(KC.Q),
        "´":KC.LBRC,
    }
    newKeys = []
    
    for key in keyList:
        if type(key) == str:
            newKeys.append(keyDefinition.get(key, KC.NO))
        else:
            newKeys.append(key)
    return newKeys
