import board
import storage
from kmk.kmk_keyboard import KMKKeyboard

from kmk.modules.split import Split
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap

from kmk.extensions.media_keys import MediaKeys

from kmk.scanners import DiodeOrientation

def getBoard():
    fsName = storage.getmount("/").label
    
    all_boards = [
        splitKb(),
    ]

    for kb in all_boards:
        if fsName.startswith(kb.fsId):
            return kb
    return None

def splitKb():
    self = KMKKeyboard()
    self.fsId = "SPLITKB"

    split = Split(
        data_pin=board.GP17,
        data_pin2=board.GP16,
        uart_flip=True,
        use_pio=True
    )

    self.modules.append(split)
    self.modules.append(Layers())
    self.modules.append(HoldTap())

    self.extensions.append(MediaKeys())

    self.col_pins = [board.GP10,board.GP11,board.GP12, board.GP13, board.GP14, board.GP15]
    self.row_pins = [board.GP21,board.GP20,board.GP19,board.GP18]

    self.diode_orientation = DiodeOrientation.COL2ROW
    self.coord_mapping = [
        00, 01, 02, 03, 04,         28, 27, 26, 25, 24,
        06, 07, 08, 09, 10,         34, 33, 32, 31, 30,
        12, 13, 14, 15, 16,         40, 39, 38, 37, 36,
                    21, 22, 23, 47, 46, 45
    ]
    return self
