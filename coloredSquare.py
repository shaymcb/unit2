#Shaylee McBride
#2Feb2018
#coloredSquare.py - idk

from ggame import *
from random import randint

rand = randint(1,4)
size = randint(100,500)

if rand == 1:
    color = Color(0xFF0000, 1)
if rand == 2:
    color = Color(0x00FF00, 1)
if rand == 3:
    color = Color(0x0000FF, 1)
if rand == 4:
    color = Color(0xFFFF00, 1)

line = LineStyle(3,color)
rectangle = RectangleAsset(size,size,line,color)
    
Sprite(rectangle)
myApp = App()
myApp.run()