"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random
from typing_extensions import Type


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nWelcome to the guessing game!")

    bounds = False
    while not bounds:
        try:

            print("A number between _ and 20 ?")
            lowerBound = input("Enter a lower bound: ")
            lowerBound = int(lowerBound)
            print(f"OK then, a number between {lowerBound} and 20 ?")
            bounds = True

        except (ValueError, TypeError):
            print("enter a number")

    actualNumber = random.randint(lowerBound, 20)
    guessed = False

    while not guessed:

        try:
            guessedNumber = input("Guess a number: ")
            guessedNumber = int(guessedNumber)
            print(f"You guessed {guessedNumber}")

            if guessedNumber == actualNumber:
                print(f"Correct! It was {actualNumber}")
                guessed = True

            elif guessedNumber < lowerBound or guessedNumber > 20:
                print("number outside the bound")

            elif guessedNumber < actualNumber:
                print("Too small, try again :'(")

            else:
                print("Too big, try again :'(")

        except (
            ValueError,
            TypeError,
        ):
            print("error this not a number")

    return "You got it!"


if __name__ == "__main__":
    print(advancedGuessingGame())

