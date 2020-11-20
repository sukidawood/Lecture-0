
from gfxhat import lcd,  fonts, backlight
from PIL import Image, ImageFont, ImageDraw
from click import getchar 


def clearBacklight():
    backlight.set_all(0,0,0)
    backlight.show()

def clearScreen(lcd):
    lcd.clear()
    lcd.show()



def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    text = 'Etch-a-Sketch'
    w, h = font.getsize(text)
    x = (width-w)//2
    y = (height - h)//2

    
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()

displayText('Etch a Sketch', lcd,x=1,y=1)


def etchSketch(x=1,y=1,pixel=1):
    while True:
        inp = getchar()
        lcd.set_pixel(x,y,1)
        lcd.show()
        if inp == 's':
            clearScreen(lcd)
        if inp == '\x1b[A':
            print("up key")
            y = y-1
            if y == 0:
                y = 63
            lcd.set_pixel(x,y,1)
            lcd.show()
        elif inp == '\x1b[B':
            print("down key")
            y = y + 1
            if y == 63:
                y = 0
            lcd.set_pixel(x,y,1)
            lcd.show()
        elif inp == '\x1b[C':
            print("right key")
            x = x + 1
            if x == 127:
                x = 0
            lcd.set_pixel(x,y,1)
            lcd.show()
        elif inp == '\x1b[D':
            print("left key")
            x = x -1
            if x == 0:
                x = 127
            lcd.set_pixel(x,y,1)
            lcd.show()

etchSketch()





