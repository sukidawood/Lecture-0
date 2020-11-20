from gfxhat import lcd,  fonts, backlight
from PIL import Image, ImageFont, ImageDraw
from click import getchar 
# import lab9

f1 =  [
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[1,0,1,1,1,1,0,1],
[1,0,0,1,1,0,0,1],
[1,0,0,1,1,0,0,1],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0]
]

pm = [[0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

xCoord = 1
yCoord = 1
def displayObject(obj,x,y):
    while True:
        lcd.clear()
        xc = x
        obj = int(input("Press 1 for ship, 2 to clear, 3 for pacman, or 4 to exit: "))
        
        if obj == 2:
            clearScreen(lcd)
        elif obj == 1:
            obj = f1
            for y1 in obj:
                for x2 in y1:
                    if x2==1:
                        pixel = 1
                    else:
                        pixel = 0
                    lcd.set_pixel(xc,y,pixel)
                    xc = xc + 1
                y = y + 1
                lcd.set_pixel(xc,y,pixel)
                xc = x

            lcd.show()
        elif obj == 3:
            obj = pm
            for y1 in obj:
                for x2 in y1:
                    if x2==1:
                        pixel = 1
                    else:
                        pixel = 0
                    lcd.set_pixel(xc,y,pixel)
                    xc = xc + 1
                y = y + 1
                lcd.set_pixel(xc,y,pixel)
                xc = x
            lcd.show()
        
        else:
            break

displayObject(obj=f1, x=xCoord,y=yCoord)



# def mainMenu():
#     print()
#     choose = input()

# 
#     if choose == '2':
#         lcd.clear()
#         lcd.show()
#         obj = int(input("Press 1 for ship, 2 to clear, 3 for pacman, or 4 to exit: "))
#         if obj == 1:
#             obj = f1
#         elif obj == 2:
#             lcd.clear()
#         elif obj == 3:
#             obj = pm
#         else:
#             obj = int(input("Enter valid input. Press 1 for ship, 2 to clear, 3 for pacman, or 4 to exit: "))
#         for y1 in obj:
#             for x2 in y1:
#                 lenY = len(obj)
#                 lenX = len(y1) 
#         xCoord = int(input("Enter the x coordinate between 0 and 127: "))
#         yCoord = int(input("Enter the y coordinate between 0 and 68"))

#         

#         if totalX > 127:
#             xCoord = int(input("Enter the x coordinate between 0 and 127: "))
#             displayObject(obj,xCoord,yCoord)
#         elif totalY > 63:
#             yCoord = int(input("Enter the y coordinate between 0 and 68"))
#             displayObject(obj,xCoord,yCoord)
#         else:
#             displayObject(obj,xCoord,yCoord)
#         mainMenu()







        


        # displayObject(obj=f1,x=12,y=8)
        







