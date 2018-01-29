#Shaylee McBride
#29Jan2018
#gradeCalculator.py - input grade and it gives you letter

grade = float(input('Input your grade: '))

if grade > 90:
    print('You got an A. Whoop-dee-doo.')
elif grade > 80:
    print("You got a B. That's not the worst.")
elif grade > 70:
    print("You got a C. You suck at life.")
elif grade > 60:
    print("You got a D. Might as well quit school.")
else:
    print("You failed. Nice!")