#Shaylee McBride
#30Jan2018
#adventure.py - choose your own adventure

print('You are bored in french class.')
print('You think you hear something crash into the trees behind the turf out the window behind you.')
print('You look out and see the whole forest glow bright green for a second before it disappears and returns to normal.')
choice1 = input('Did you imagine it? ')
if choice1 == 'yes':
    print('You decide it was just your mind playing tricks on you. You go back to learning le subjonctif and live a boring life.')
    print("THE END")
if choice1 == 'no':
    print('You look closer and see a huge metal spike emerging out of the woods where you thought you saw the light.')
    print('The top of the spike lights up an ominous red. This is so cool!')
    print('Suddenly your ears fill with a high-pitched ringing noise. You look around-- everyone else is continuing to discuss the reign of Napoleon III as if nothing is wrong.') 
    print("The sound grows and grows until it is excruciatingly loud. You can't form thoughts. You fall to the ground, clutching your ears and screaming.")
    print("How has nobody noticed you're having a fit? It's not like you're being quiet.")
    choice2 = input("Do you: (a) Try harder to get someone's attention, (b) Wait it out (c) Walk to the nurse's (d) Jump out the window towards the mysterious spike ")
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
        print("You decide to try to get out the window. It's right next to you, but you hardly make it-- your legs feel too weak for you to walk.")
        print("As soon as you get the window open and breathe the fresh air, the noise goes away.")
        print("A wispy tendril reaches out from the spike and grabs you. It pulls you in.")
        print("You find yourself in a round metal windowless room full of a clear jelly. You sink into the jelly-- you cannot breathe and struggle to get out.")
        print("Suddenly all the jelly recedes. It forms into a blob beside you. You watch in horror as it takes shape and gains color, becoming a perfect copy of you.")
        print("'What's going on?' you yell. 'What's going on?' not-you yells back in your voice. Then it runs unsteadily out through a hatch you hadn't noticed and into the school.")
        print("'What the fuck', you say. What do you do now?"
        

