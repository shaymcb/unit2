#Shaylee McBride
#2Feb2018
#newColor.py - because the last one pissed me off so much that I learned for loops

from ggame import *
from random import randint

color = '0x'

for i in range(0,6):
    rand = randint(0,15)
    if rand < 10:
       rand = str(rand)
    elif rand == 10:
        rand = 'A'
    elif rand == 11:
        rand = 'B'
    elif rand == 12:
        rand = 'C'
    elif rand == 13:
        rand = 'D'
    elif rand == 14:
        rand = 'E'
    else:
        rand = 'F'
    color = color+rand

print(color)
colorSquare = Color(color, 1)

size = randint(100,500)
line = LineStyle(3,colorSquare)
rectangle = RectangleAsset(size,size,line,colorSquare)
    
Sprite(rectangle)
myApp = App()
myApp.run()
