#Shaylee McBride
#2Feb2018
#coloredSquare.py - idk

from ggame import *
from random import randint

rand = randint(0,15)
n = 0

if n < 6:
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

color = '0x'+rand


#size = randint(100,500)
#line = LineStyle(3,colorLine)
#rectangle = RectangleAsset(size,size,line,colorSquare)
    
#Sprite(rectangle)
#myApp = App()
#myApp.run()