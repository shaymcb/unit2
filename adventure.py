#Shaylee McBride
#30Jan2018
#adventure.py - choose your own adventure

print('You are bored in french class when you think you hear something crash into the trees behind the turf out the window behind you.')
choice1 = input('Did you imagine it? (yes/no)')
if choice1 == 'yes':
    print('You decide it was just your mind playing tricks on you. You go back to learning le subjonctif and live a boring life.')
    print("THE END")
if choice1 == 'no':
    print('You look closer and see a huge metal spike emerging out of the woods where you thought you saw the light. The top of the spike lights up an ominous red. Suddenly your ears fill with a high-pitched ringing noise.') 
    print("The sound becomes excruciatingly loud. You fall to the ground, clutching your ears and screaming. How has nobody noticed this?")
    choice2 = input("Do you: (a) Try to get someone's attention, (b) Wait it out (c) Walk to the nurse's (d) Jump out the window towards the mysterious spike ")
    if choice2 == 'a':
        print("Still lying on the ground, you whack the leg of the person sitting next to you.")
        print("'Claire!' you yell, 'get help!'")
        print("She rubs her leg and looks confused. She doesn't see or hear you. No one does. You're gonna need to do something more drastic.")
        choice3 = input("Do you (a) Shake Claire until she realizes something weird is going on, or (b) Give up and try to get out of there? ")
        if choice3 == 'b':
            choice2 = 'd'
        else:
            print("You shake Claire and yell in her face. 'Help me!' she screams, 'I don't know what's going on!")
            print("Everyone thinks Claire is having a seizure. They call 911.")
            print("When the paremedics arrive, you try to get their attention, but they don't notice you.")
            choice2 = 'b'
    elif choice2 == 'c':
        print("Your legs feel like jelly. You can't walk. You try to creep toward the door but you can't make it.")
        choice2 == 'b'
    if choice2 == 'b':
        print("Your head feels like it's splitting open. You pass out and never wake back up.")
        print("THE END")
    if choice2 == 'd':
        print("As soon as you get the window open, the noise stops. A wispy tendril reaches out from the spike pulls you in.")
        print("You find yourself in a round metal windowless room full of a clear jelly. You sink into the jelly-- you cannot breathe and struggle to get out.")
        print("Suddenly all the jelly recedes. You watch in horror as it takes shape and gains color, forming a perfect copy of you.")
        print("'What's going on?' you scream. 'What's going on?' not-you screams back in your voice. Then it runs unsteadily out a hatch and into the school.")
        print("The hatch closes behind it, leaving you trapped. 'What the fuck', you say. What do you do now?")
        choice3 = input("(a) Try to break open the hatch and escape, (b) Call for help, or (c) Wait for not-you to return ")

