#Shaylee McBride
#2Feb2018
#slope2.py - finds slope given two points, also says if fail

x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))
slope = (y2 - y1)/(x2 - x1)

if x1 == x2:
    print('The slope is infinite.')
else:
    print("The slope is",slope)
    print('The equation of the line is y =',slope,'x +',y1-slope*x1)
