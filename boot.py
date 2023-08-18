import board

from kmk.bootcfg import bootcfg

bootcfg(
    sense=board.GP10,  # column
    source=board.GP21, # row
    mouse=False,
    storage=False,
    usb_id=('KMK Keyboards', 'Custom 34 split'),
)
