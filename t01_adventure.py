######################################################################
# Author: Samantha Schweinsberg and Jacob Barns     TODO: Change this to your names
# Username: barns schweinsbergs              TODO: Change this to your usernames
#
# Assignment: T01: Choose Your Own Adventure
#
# Purpose: To create a choose-your-own-adventure style game.
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
#   Inspired by https://www.cs.hmc.edu/twiki/bin/view/CS5/Week0ChoiceProblem
######################################################################
from time import sleep

delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False         # You start out not dead, which is good.

# Asks the user to input their name.
username = input("What do they call you, unworthy adversary? ")

#########################################################################################################
# The following is the first part of the story. Don't change this section.
print()
print("Welcome,", username, ", to the labyrinth.")
sleep(delay)
print("Before you lies two paths. One path leads to treasures of unimaginable worth.")
print("The other, certain death. Choose wisely.")
print()
sleep(delay * 2)
print("You are in a dark cave. You can see nothing.")
print("Staying here is certainly not wise. You must find your way out.")
print()
sleep(delay)

#########################################################################################################
# This is an example chapter. Your story will follow a similar structure.
# You will learn more by NOT copy and pasting this section. Write your section on your own, and when you get stuck,
# refer to this code to help you get unstuck. Of course, raise your hand if you get really stuck.

direction = input("Which direction would you like to go? [North/South/East/West]" )

if direction == "North":
    # Good choice!
    print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
    sleep(delay)
elif direction == "South":
    # Oh... Bad choice
    print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
    sleep(delay)
    print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
    print("Running seems like a good idea now. But... it's really, really dark.")
    print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
    print("He eats you. You are delicious.")
    dead = True
else:
    # Neutral choice
    print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
    sleep(delay)

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

#########################################################################################################
# TODO Add your part of the story here. Keep in mind you may NOT be coming right after the example above.

print("You ntinue on with your journey. You happen to stumble across a bomb.")
print("One of the people offer you wirecutters. With nothing to lose, you decide to be a hero.")
print("You unscrew the bomb. In front of you are three wires: red, blue, and yellow.")
sleep(delay * 5)
print("What will you do,", username,"?")
color = input("Red, Blue, or Yellow?")

if color == "Red":
    #The good choice
    print("You suck in a breath and then cut the wire. The LEDs flicker, then shut off. You did it!")

elif color == "Blue":
    #The bad choice
    print("You suck in a breath and then cut the wire. The bomb explodes into a white light. You die instantly.")
    dead = True

else:
    #neutral choice
    print("You suck in a breath and cut the yellow wire.")
    print("")
    print("Nothing explicitly happens, but suddenly you have a loaf of banana nut bread in your pocket.")
    print("... You decide to move on.")








# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################

# The following is the end of the story. Don't change this section, unless you really want to
# (though it may not be used in the final story. Or will it...)
print("Look at that! You made it to the end of the story without dying! ")
print("Congratulations... now go play again and find an interesting way to perish. ")
print("Try again by hitting the green play button.")
