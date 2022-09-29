import re
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luna.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from PIL import Image, ImageDraw

def main(cascaded, block_orientation, rotate):
    # create matrix device
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, cascaded=cascaded or 1, bloque_orientation=block_orientation, rotate=rotate or 1)
    #debugging purpose
    print("[-] Matriz initialized")
    img = canvas(device,background=None,dither=True)
    draw = ImageDraw.Draw(img)
    draw.line((0, 0) + img.size, fill=128)
    print("Dibujo realizado")

if __name__ == "__main__":
    #cascaded = Number of cascaded MAX7219 LED matrices, default=1
    #block_orientation = choices 0,90,-90, Corrects block orientation when wired vertically, default= 0
    #rotate = choices 0,1,2,3, Rotate display 0=0°, 1=90°, 2=180°, 3=270°, default=0

    try:
        main(cascaded=0, block_orientation=180, rotate=3)
    except KeyboardInterrupt:
        pass