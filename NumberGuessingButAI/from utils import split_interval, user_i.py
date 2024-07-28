from utils import split_interval, user_input    
# Defining the variables
lower_interval = 1
upper_interval = 11
feedback = None

while feedback != "=":

    guess = split_interval(lower_interval, upper_interval)
    input_response = user_input(guess)

    if input_response == "<":
        upper_interval = guess
    elif input_response == ">":
        lower_interval = guess
    else:
        if input_response == "=":
            print("That's it!")