#Andrew Tkacs

#Lab 11-3

import random  #this imports a random number for me so the user can guess it.

def number_guess():
    generated_number = random.randint(1, 100)

    guessed_correctly = False #while loop that gives the user feedback based on their guess.
    while not guessed_correctly:
        user_guess = int(input("Guess the number between 1 and 100: "))

        if user_guess == generated_number:
            print("Congratulations! You guessed the correct number.")
            guessed_correctly = True
        else:
            if user_guess < generated_number:
                print("Incorrect! The number is higher than your guess. Try again.")
            else:
                print("Incorrect! The number is lower than your guess. Try again.")

number_guess()


