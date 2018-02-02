#Shaylee McBride
#2Feb2018
#ageCalculator.py - for those of you that have a panic attack when the airport staff asks how old you are

from datetime import date

year = int(input('Enter the year you were born: '))
month = int(input('Enter the month you were born (as a number): '))
day = int(input('Enter the day you were born: '))

if month > date.today().month or (month == date.today().month and day > date.today().day):
    print('You are',date.today().year - year - 1,'years old')
else:
    print('You are',date.today().year - year,'years old')
if month == date.today().month and day == date.today().day:
    print('Happy Birthday!')
