import board
from boards import getBoard
from utilities import convert, LayerCreator, HT
from kmk.keys import KC


keyboard = getBoard()

lc = LayerCreator()

Home = lc.create_layer()
Number = lc.create_layer() 
Nav = lc.create_layer() 
Fn = lc.create_layer() 
Symbol = lc.create_layer() 

HomeLy = KC.TO(Home.id)
NumberLy = KC.TG(Number.id)
NavLy = KC.MO(Nav.id)
FnLy = KC.TG(Fn.id)
SymbolLy = KC.TG(Symbol.id)

keyboard.keymap = [
    [
        KC.Q,                KC.W,  KC.E,   KC.R,               KC.T,                                                           KC.Y,                KC.U,     KC.I,      KC.O, KC.P,
        KC.A,                KC.S,  KC.D,   KC.F,               KC.G,                                                           KC.H,                KC.J,     KC.K,      KC.L, KC.SCLN,
        HT(KC.Z,KC.LSFT),    KC.X,  KC.C,   KC.V,               KC.B,                                                           KC.N,                KC.M,  KC.COMM,    KC.DOT, HT(KC.ENT,KC.LSFT),
                                            HT(KC.ESC,NavLy),   HT(SymbolLy, KC.LGUI),   HT(NumberLy, KC.LALT),   KC.BSPC,    KC.SPC,   HT(FnLy, KC.LCTL),
    ],
    # number layer
    convert([
            KC.NO,       KC.BRIU,  KC.VOLU,      KC.MNXT,  KC.NO,                           "+",     KC.N7,     KC.N8,       KC.N9,        "*",
            KC.NO,       KC.NO,    KC.MUTE,      KC.MPLY,  KC.NO,                           "-",     KC.N4,     KC.N5,       KC.N6,        "/",
            KC.NO,       KC.BRID,  KC.VOLD,      KC.MPRV,  KC.NO,                           "^",     KC.N1,     KC.N2,       KC.N3,     KC.ENT,
                                                 KC.NO,   HomeLy,    KC.NO,     KC.NO,    KC.N0,    KC.DOT,
    ]),
    # nav layer
    [
            KC.NO,       KC.NO,       KC.NO,       KC.NO,     KC.NO,                         KC.NO,     KC.NO,       KC.NO,     KC.NO,    KC.NO,
            KC.NO,       KC.NO,       KC.NO,       KC.NO,     KC.NO,                         KC.LEFT, KC.DOWN,       KC.UP,   KC.RGHT,    KC.NO,
            KC.NO,       KC.NO,       KC.NO,       KC.NO,     KC.NO,                         KC.NO,     KC.NO,       KC.NO,     KC.NO,   KC.ENT,
                                                   KC.NO,    HomeLy,    KC.NO,       KC.NO,  KC.TAB,   KC.DEL,
    ],
    # mod layer
    convert([
           KC.NO,       KC.F1,       KC.F2,       KC.F3,     KC.NO,                       KC.NO,   KC.F7,       KC.F8,     KC.F9,    KC.NO,
           KC.NO,       KC.F4,       KC.F5,       KC.F6,     KC.NO,                       KC.NO,  KC.F10,      KC.F11,    KC.F12,   KC.NO,
           KC.NO,       KC.NO,       KC.NO,       KC.NO,     KC.NO,                       KC.NO,   KC.NO,       KC.NO,     KC.NO,    KC.NO,
                                                  KC.NO,    HomeLy,   KC.NO,       KC.NO, KC.NO,   KC.NO,
    ]),
    convert([
           "",        "_",       "-",         "=",       "~",                         "/",     "{",   "'",   "}",  "\\",
           "!",       "#",       "$",         "%",       "&",                         "<",     "(",   '"',   ")",  ">",
           "¡",        "",        "",          "",       "|",                         "¿",     "[",   "`",   "]",  "?",
                                            KC.NO,    HomeLy,   KC.NO,       KC.NO, KC.NO, KC.LSFT,
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
