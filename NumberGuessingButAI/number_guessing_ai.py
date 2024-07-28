def user_input(guess):
    """ Takes user's input and compares it to AI's guess,
    and returns the truth.
    """
    feedback = input("Is your number smaller (<), larger (>), or equal to (=) my guess? %d"%(guess))
    while not (feedback == "<" or feedback == ">" or feedback == "="):
        feedback = input("Is your number smaller (<), larger (>), or equal to (=) my guess?%d"%(guess))

    return feedback
    

def split_interval(lower_interval, upper_interval):
    """ Takes lower limit and higher limit,
    and returns the mid point as x. """
    lower_interval = round(lower_interval)
    upper_interval = round(upper_interval)
    mid_interval = (upper_interval + lower_interval)/2
    return mid_interval

# Defining the variables
lower_interval = 1
upper_interval = 11
feedback = None
wanna_play = True
number_of_guesses = 0
while wanna_play:

    while feedback != "=":
        number_of_guesses += 1 
        guess = split_interval(lower_interval, upper_interval)
        feedback = user_input(guess)

        if feedback == "<":
            upper_interval = guess
        elif feedback == ">":
            lower_interval = guess
        else:
            if feedback == "=":
                print("That's it!, AI tried %d times till success."%(number_of_guesses))
    play_more = input("Wanna play more? Y/N: ")
    if play_more == "N" or play_more == "n":
        wanna_play = False
        print("See you soon!")