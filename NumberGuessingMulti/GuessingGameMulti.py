import random

computer_guess = random.randint(1,10)
attempts = 0
MAX_ATTEMPTS = 5
want_to_play = True
best_score = MAX_ATTEMPTS
times_played = 0
while want_to_play:
    times_played = times_played + 1
    user_guess = int(input("Please guess a number: "))

    while user_guess != computer_guess and attempts != MAX_ATTEMPTS:
    
        if user_guess != computer_guess:
         attempts = 1 + attempts
        if user_guess > computer_guess:
            print("That's High")
        if user_guess < computer_guess:
            print("That's low")
        user_guess = int(input("Try Again!, you've got %d more attempts: "%((MAX_ATTEMPTS + 1) - attempts)))

    if user_guess == computer_guess:
         print("Jackpot!, took you %d attempts"%attempts)
         
    else:
        print("Uh, Better luck next time.")
    wanna_play = input("Best score yet:%d, Wanna play more? y/n: "%(best_score)) 
    attempts = 0   
    if wanna_play == "n" or wanna_play == "N":
        want_to_play = False
print("Thanks for playing!%d times played"%(times_played))