#Shaylee McBride
#30Jan2018
#adventure.py - choose your own adventure

print('You are bored in french class when you think you hear something crash into the trees behind the turf out the window behind you.')
choice1 = input('Did you imagine it? (yes/no) ')
if choice1 == 'yes':
    print("You decide it was just your mind playing tricks on you. You go back to learning le subjonctif and live a boring life. Some aliens take over the world a few weeks later, but it doesn't really affect you.")
    print("THE END")
if choice1 == 'no':
    print("You look closer and see a huge metal spike emerging out of the woods where you thought you saw the light. Your ears fill with a high-pitched ringing noise. The sound becomes excruciatingly loud. You fall to the ground, clutching your ears and screaming, but nobody seems to notice.")
    choice2 = input("Do you: (a) Try to get someone's attention, (b) Wait it out (c) Walk to the nurse's (d) Jump out the window towards the mysterious spike ")
    if choice2 == 'a':
        print("Still lying on the ground, you whack the leg of the person sitting next to you.")
        print("'Claire!' you yell, 'get help!'")
        print("She rubs her leg and looks confused. She doesn't see or hear you. No one does. You're gonna need to do something more drastic.")
        choice3 = input("Do you (a) Shake Claire until she realizes something weird is going on, or (b) Give up and try to get out of there? ")
        if choice3 == 'b':
            print("Your legs feel like jelly. You can't walk. You try to creep toward the door but you can't make it.")
            print("Your head feels like it's splitting open. You pass out and never wake back up.")
            print("THE END")
        else:
            print("You shake Claire and yell in her face. 'Help me!' she screams, 'I don't know what's going on!")
            print("Everyone thinks Claire is having a seizure. They call 911.")
            print("When the paremedics arrive, you try to get their attention, but they don't notice you.")
            print("Your head feels like it's splitting open. You pass out and never wake back up.")
            print("THE END")
    elif choice2 == 'c':
        print("Your legs feel like jelly. You can't walk. You try to creep toward the door but you can't make it.")
        print("Your head feels like it's splitting open. You pass out and never wake back up.")
        print("THE END")
    elif choice2 == 'b':
        print("Your head feels like it's splitting open. You pass out and never wake back up.")
        print("THE END")
    elif choice2 == 'd':
        print("As soon as you get the window open, the noise stops. A wispy tendril reaches out from the spike and pulls you in.")
        print("You find yourself in a round metal windowless room surrounded by a clear jelly. You cannot breathe and struggle to get out. Suddenly all the jelly recedes. You watch in horror as it takes shape and gains color, forming a perfect copy of you.")
        print("'What's going on?' you scream. 'What's going on?' not-you screams back in your voice. Then it runs unsteadily out a hatch and into the school.")
        print("The hatch closes behind it, leaving you trapped. 'What,' you say. What do you do now?")
        choice4 = input("(a) Try to break open the hatch and escape, (b) Call for help, or (c) Wait for not-you to return ")
        if choice4 == 'b':
            print("Somehow you have reception. Whatever the blob was, it didn't plan on cell phones.")
            choice5 = input('Do you call (a) your friend, (b) your mom, or (c) 9-1-1? ')
            if choice5 == 'c': 
                print("'Do you think I was born yesterday?' the operator says. She doesn't believe you.")
                choice5 = input('Try someone else.')
            if choice5 == 'b':
                print("Your mom doesn't pick up the phone. 'Damn it!' you yell, and something inside the room electrocutes you for talking too loud.")
                print("THE END")
            elif choice5 == 'a':
                print("Your friend picks up on one ring. It's so nice to have people you can count on. 'Tish!' you say, 'I need help.'")
                print("'Aren't you be in French?' she asks 'I'm not helping you cheat.'")
                print("'No, it's not that' you say. 'I think I've been body-snatched. Go see if I'm in class.' 'If you're fucking with me...' Tish says, but checks anyway.")
                print("'What-- What--,' says Tish, 'You're there, but you're talking to me, but you're not talking to me but---'")
                print("She believes you now, comes to rescue you, and helps you save the world from an alien invasion, but I'm out of space so you don't get to read about it.")
                print("THE END")
        elif choice4 == 'a':
            print("You bang on the hatch but it doesn't open. It does, however sense your presence and squish you into the floor.")
            print("THE END")
