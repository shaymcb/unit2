#Shaylee McBride
#31Jan2018
#warmup.py - divisible tests

num = int(input("Enter a number: "))

if num%6 == 0:
    print(num,'is divisible by both 2 and 3.')
elif num%3 == 0:
    print(num,'is divisible by 3.')
elif num%2 == 0:
    print(num,'is divisible by 2.')
else:
    print(num,'is not divisible by 2 or 3.')
