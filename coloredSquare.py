#Shaylee McBride
#2Feb2018
#coloredSquare.py - idk

from ggame import *
from random import randint

colorSquare = Color(hex(randint(0,256**3-1)), 1)
colorLine = Color(hex(randint(0,256**3-1)), 1)

size = randint(100,500)
line = LineStyle(3,colorLine)
rectangle = RectangleAsset(size,size,line,colorSquare)
    
Sprite(rectangle)
myApp = App()
myApp.run()