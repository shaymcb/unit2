#Shaylee McBride
#12Feb2018
#quiz2.py - words

word1 = input('Enter a word: ')
word2 = input('Enter another word: ')

if len(word1) == len(word2):
    print('The words are the same length.')
elif len(word1) > len(word2):
    print(word1,'has more letters than',word2)
else:
    print(word2,'has more letters than',word1)

if 'p' in word1 and 'p' in word2:
    print('Both words have a p in them. Wow!')
elif 'p' in word1:
    print(word1,'has a p in it')
elif 'p' in word2:
    print(word2,'has a p in it')
else:
    print("there are no p's in either word :(")

print("Now enter two numbers that add up to twelve.")
num1 = float(input("First number: "))
num2 = float(input("Second number: "))

if num1 + num2 == 12:
    print('Nice job! You can do simple arithmetic.')
else:
    print('WRONG')
