#Shaylee McBride
#5Feb2018
#quadratic.py - quadratic formula

from math import sqrt

print('Ex: ax^2 + bx + c')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

discriminant = b**2 - 4*a*c

if discriminant >= 0:
    print('x =',(-b + sqrt(discriminant))/(2*a),'or')
    print('x =',(-b - sqrt(discriminant))/(2*a))
if discriminant < 0:
    print('x =',-b/(2*a),'+',sqrt(-discriminant)/(2*a),'i or')
    print('x =',-b/(2*a),'-',sqrt(-discriminant)/(2*a))