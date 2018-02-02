#Shaylee McBride
#2Feb2018
#coloredSquare.py - idk

from ggame import *
from random import randint

rand = randint(1,4)

red = Color(0xff0000, 1)
line = LineStyle(3,red)
rectangle = RectangleAsset(100,100,line,red)

Sprite(rectangle)
myApp = App()
myApp.run()