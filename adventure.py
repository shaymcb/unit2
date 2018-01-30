#Shaylee McBride
#30Jan2018
#adventure.py - choose your own adventure

print('You are bored in french class.')
print('You think you hear something crash into the trees behind the turf out the window behind you.')
print('You look out and see the whole forest glow bright green for a second before it disappears and returns to normal.')
choice1 = input('Did you imagine it? ')
if choice1 == 'yes':
    print('You decide it was just your mind playing tricks on you. You go back to learning le subjonctif and live a boring life.')
else:
    print('You look closer and see a huge metal spike emerging out of the woods where you thought you saw the light.')
    print('The top of the spike lights up an ominous red. This is so cool!')
    print('Suddenly your ears fill with a high-pitched ringing noise. You look around-- everyone else is continuing to discuss the reign of Napoleon III as if nothing is wrong.') 
    print("The sound grows and grows until it is excruciatingly loud. You can't form thoughts. You fall to the ground, clutching your ears and screaming.")
    print("How has nobody noticed you're having a fit? It's not like you're being quiet.")
    choice2 = input("Do you: (a) Try harder to get someone's attention, (b) Wait it out (c) Walk the the nurse's (d) Jump out the window)
    if choice2 == 'a':
        print("Still lying on the ground, you whack the leg of the person sitting next to you.")
        print("'Claire!' you yell, 'get help!'")
        print("She rubs her leg and looks confused. She doesn't see or hear you. No one does. You're gonna need to do something more drastic.")
        choice3 = input("Do you (a) Shake Claire until she realizes something weird is going on, or (b) Give up and try to get out of there")
        if choice3 == 'b':
            choice2 = 'd'
        else:
            print

