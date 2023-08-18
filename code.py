import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap

split = Split(
    data_pin=board.GP17,
    data_pin2=board.GP16,
    uart_flip=True,
    use_pio=True
)

holdTap = HoldTap()
def HT(tap, hold):
    return KC.HT(tap, hold, prefer_hold=True, tap_interrupted=False, tap_time=300)

keyboard = KMKKeyboard()
keyboard.modules.append(split)
keyboard.modules.append(Layers())
keyboard.modules.append(holdTap)

keyboard.col_pins = [board.GP10,board.GP11,board.GP12, board.GP13, board.GP14, board.GP15]
keyboard.row_pins = [board.GP21,board.GP20,board.GP19,board.GP18]
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.coord_mapping = [
      0,      1,     2,      3,      4,                     28,     27,     26,     25,     24,
      6,      7,     8,      9,     10,                     34,     33,     32,     31,     30,
     12,     13,    14,     15,     16,                     40,     39,     38,     37,     36,
                             21,    22,     23,     47,     46,     045,
]

HomeLy = KC.TO(0)
NumberLy = KC.TG(1)
NavLy = KC.MO(2)
FnLy = KC.TG(3)
SymbolLy = KC.TG(4)

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

keyboard.keymap = [
    [
            KC.Q,                KC.W,                 KC.E,                KC.R,                  KC.T,                             KC.Y,   KC.U,                KC.I,                KC.O,                 KC.P,
            KC.A,                HT(KC.S,KC.LCTRL),    HT(KC.D,KC.LALT),    HT(KC.F,KC.LGUI),      KC.G,                             KC.H,   HT(KC.J,KC.RGUI),    HT(KC.K,KC.RALT),    HT(KC.L,KC.RCTRL),    KC.SCLN,
            HT(KC.Z,KC.LSFT),    KC.X,                 KC.C,                KC.V,                  KC.B,                             KC.N,   KC.M,                KC.COMM,             KC.DOT,               HT(KC.ENT,KC.LSFT),
                                                                            HT(KC.ESC,NavLy),  SymbolLy,    NumberLy,    KC.BSPC,  KC.SPC,   FnLy,
    ],
    # number layer
    convert([
            KC.NO,       KC.NO,      KC.NO,      KC.NO,    KC.NO,                         "+",    KC.N7,     KC.N8,       KC.N9,        "*",
            KC.NO,       KC.NO,      KC.NO,      KC.NO,    KC.NO,                         "-",    KC.N4,     KC.N5,       KC.N6,        "/",
            KC.NO,       KC.NO,      KC.NO,      KC.NO,    KC.NO,                         "^",    KC.N1,     KC.N2,       KC.N3,     KC.ENT,
                                                 KC.NO,    KC.NO,    KC.NO,    HomeLy,    KC.N0,    KC.DOT,
    ]),
    # nav layer
    [
            KC.NO,       KC.NO,       KC.NO,       KC.NO,     KC.NO,                         KC.NO,     KC.NO,       KC.NO,     KC.NO,    KC.NO,
            KC.NO,       KC.NO,       KC.NO,       KC.NO,     KC.NO,                         KC.LEFT,   KC.DOWN,     KC.UP,     KC.RGHT,  KC.NO,
            KC.NO,       KC.NO,       KC.NO,       KC.NO,     KC.NO,                         KC.NO,     KC.NO,       KC.NO,     KC.NO,    KC.ENT,
                                                   KC.NO,     KC.NO,    KC.NO,      HomeLy,  KC.TAB,    KC.NO,
    ],
    # mod layer
    convert([
           KC.NO,       KC.F1,       KC.F2,       KC.F3,     KC.NO,                       KC.NO,   KC.F7,       KC.F8,     KC.F9,    KC.NO,
           KC.NO,       KC.F4,       KC.F5,       KC.F6,     KC.NO,                       KC.NO,   KC.F10,      KC.F11,    KC.F12,   KC.NO,
           KC.NO,       KC.NO,       KC.NO,       KC.NO,     KC.NO,                       KC.NO,   KC.NO,       KC.NO,     KC.NO,    KC.NO,
                                                  KC.NO,     KC.NO, KC.LSFT,      HomeLy, KC.NO,   KC.NO,
    ]),
    convert([
           "",        "_",       "-",         "=",       "~",                         "/",     "{",   "'",   "}",  "\\",
           "!",       "#",       "$",         "%",       "&",                         "<",     "(",   '"',   ")",  ">",
           "¡",        "",        "",          "",       "|",                         "¿",     "[",   "`",   "]",  "?",
                                            KC.NO,     KC.NO,   KC.NO,      HomeLy, KC.NO, KC.LSFT,
    ]),
   #convert(
   #[
   #        KC.NO,       KC.NO,       KC.NO,       KC.NO,     KC.NO,                       KC.NO,   KC.NO,       KC.NO,     KC.NO,    KC.NO,
   #        KC.NO,       KC.NO,       KC.NO,       KC.NO,     KC.NO,                       KC.NO,   KC.NO,       KC.NO,     KC.NO,    KC.NO,
   #        KC.NO,       KC.NO,       KC.NO,       KC.NO,     KC.NO,                       KC.NO,   KC.NO,       KC.NO,     KC.NO,    KC.NO,
   #                                               KC.NO,     KC.NO,   KC.NO,      KC.NO,  KC.NO,   KC.NO,
   #]),
]

if __name__ == '__main__':
    keyboard.go()
