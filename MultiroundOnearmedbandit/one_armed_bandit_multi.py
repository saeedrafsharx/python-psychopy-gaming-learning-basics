# import the needed libraries
import random

# Defining variables
coins = 50
wanna_keep_playing = True

# Welcome, and wanna play

# Defining a loop so player can keep plying if wannted to
while wanna_keep_playing:

    welcome = input("Welcome! Wanna roll the dice? Y/N: ")

    if welcome == "y" or welcome == "Y":

        coins += -1

        # Rolling the Dice
        slot1 = random.randint(1,6)
        slot2 = random.randint(1,6)
        slot3 = random.randint(1,6)
        # Printing the outcome
        print("The numbers are %d,%d,and %d."%(slot1,slot2,slot3))

        if slot1 == slot2 == slot3:
            coins = coins + 5
            print("Three of a kind!, you've got %d coins"%(coins))

        if slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
            coins = coins + 2
            print("That's a pair, you've got %d coins"%(coins))

        else:
            print("Better luck next time, you've got %d coins"%(coins))

        keep_playing = input("Wanna play again? Y/N: ")
        if keep_playing == "N" or keep_playing == "n":
                wanna_keep_playing = False
        if coins == 0:
            # If condition is met, set the flag to True and break out of the loop
            print("That's gameover.")
            break
    else:
        wanna_keep_playing = False
        print("See you soon.")