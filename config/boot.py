import board

from kmk.bootcfg import bootcfg
from boards import getBoard

currentBoard = getBoard()

bootcfg(
    sense=currentBoard.col_pins[0],
    source=currentBoard.row_pins[0],
    mouse=False,
    storage=False,
    usb_id=('KMK Keyboards', 'Custom 34 split'),
)
