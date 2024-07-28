""" Here lies the two functions, to find out a mid of 
    an interval, or to ask user to feedback on out guess,
    based on that interval midpoint.
"""
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