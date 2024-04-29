import board
from boards import getBoard
from utilities import LayerCreator, HT
from kmk.keys import KC
from kmk.extensions.international import International

profile = "osx"  # linux
lc = LayerCreator(profile=profile)

Home = lc.create_layer()
MainFn = lc.create_layer()
Numbers = lc.create_layer() 
Nav = lc.create_layer() 
FnKeys = lc.create_layer() 
Symbols = lc.create_layer() 

Home.set_layout(
    [
        KC.Q,             KC.W, KC.E, KC.R,              KC.T,                                    KC.Y,   KC.U, KC.I,    KC.O,   KC.P,
        KC.A,             KC.S, KC.D, KC.F,              KC.G,                                    KC.H,   KC.J, KC.K,    KC.L,   KC.SCLN,
        HT(KC.Z,KC.LSFT), KC.X, KC.C, KC.V,              KC.B,                                    KC.N,   KC.M, KC.COMM, KC.DOT, HT("-",KC.LSFT),
                                      HT(KC.ESC,Nav.MO), MainFn.MO, HT("´",Numbers.MO),  KC.BSPC, KC.SPC, KC.ENT,     
    ]
)
MainFn.set_layout(
    [
        KC.Q,            KC.W,            KC.E,               KC.R,               KC.T,                            KC.Y,                 KC.U,                KC.I,               KC.O,               KC.P,
        KC.A,            HT(KC.S,KC.LCTL),KC.HT(KC.D,KC.LGUI),KC.HT(KC.F,KC.LALT),KC.G,                            KC.H,                 KC.HT(KC.J,KC.LALT), KC.HT(KC.K,KC.LGUI),KC.HT(KC.L,KC.LCTL),KC.SCLN,
        HT(KC.Z,KC.LSFT),KC.X,            KC.C,               KC.V,               KC.B,                            KC.N,                 KC.M,                KC.COMM,            KC.DOT,             HT("-",KC.LSFT),
                                                              KC.NO,              KC.NO, KC.NO,  HT(KC.BSPC,KC.NO),HT(KC.SPC,Symbols.MO),HT(KC.ENT,FnKeys.MO),
    ]
)
Numbers.set_layout(
    [
        KC.NO,       KC.BRIU,  KC.VOLU,      KC.MNXT,  KC.NO,                           "+",     KC.N7,     KC.N8,       KC.N9,        "*",
        KC.NO,       KC.NO,    KC.MUTE,      KC.MPLY,  KC.NO,                           "-",     KC.N4,     KC.N5,       KC.N6,        "/",
        KC.NO,       KC.BRID,  KC.VOLD,      KC.MPRV,  KC.NO,                           "^",     KC.N1,     KC.N2,       KC.N3,     KC.DOT,
                                             KC.NO,    KC.NO,    KC.NO,     KC.BSPC,    KC.N0,   KC.ENT,
    ]
)
Nav.set_layout(
    [
        KC.NO,       KC.NO,       KC.NO,       KC.NO,     KC.NO,                         KC.NO,     KC.NO,       KC.NO,     KC.NO,    KC.NO,
        KC.NO,       KC.NO,       KC.NO,       KC.NO,     KC.NO,                         KC.LEFT, KC.DOWN,       KC.UP,   KC.RGHT,    KC.NO,
        KC.NO,       KC.NO,       KC.NO,       KC.NO,     KC.NO,                         KC.NO,     KC.NO,       KC.NO,     KC.NO,   KC.ENT,
                                               KC.NO,     KC.NO,    KC.NO,       KC.NO,  KC.TAB,   KC.DEL,
    ]
)
FnKeys.set_layout(
    [
        KC.NO,       KC.F1,       KC.F2,       KC.F3,     KC.NO,                       KC.NO,   KC.F7,       KC.F8,     KC.F9,    KC.NO,
        KC.NO,       KC.F4,       KC.F5,       KC.F6,     KC.NO,                       KC.NO,  KC.F10,      KC.F11,    KC.F12,   KC.NO,
        KC.NO,       KC.NO,       KC.NO,       KC.NO,     KC.NO,                       KC.NO,   KC.NO,       KC.NO,     KC.NO,    KC.NO,
                                               KC.NO,     KC.NO,   KC.NO,       KC.NO, KC.NO,   KC.NO,
    ]
)
Symbols.set_layout(
    [
        "@",       "_",       "-",         "=",       "~",                         "/",     "{",   "'",   "}",  "\\",
        "!",       "#",       "$",         "%",       "&",                         "<",     "(",   '"',   ")",  ">",
        "¡",        "",        "",          "",       "|",                         "¿",     "[",   "`",   "]",  "?",
                                         KC.NO,     KC.NO,   KC.NO,       KC.NO, KC.NO, KC.LSFT,
    ]
)
   #convert(
   #[
   #        KC.NO,       KC.NO,       KC.NO,       KC.NO,     KC.NO,                       KC.NO,   KC.NO,       KC.NO,     KC.NO,    KC.NO,
   #        KC.NO,       KC.NO,       KC.NO,       KC.NO,     KC.NO,                       KC.NO,   KC.NO,       KC.NO,     KC.NO,    KC.NO,
   #        KC.NO,       KC.NO,       KC.NO,       KC.NO,     KC.NO,                       KC.NO,   KC.NO,       KC.NO,     KC.NO,    KC.NO,
   #                                               KC.NO,     KC.NO,   KC.NO,      KC.NO,  KC.NO,   KC.NO,
   #]),


keyboard = getBoard()
keyboard.extensions.append(International())
keyboard.keymap = lc.get_layers()

if __name__ == '__main__':
    keyboard.go()
