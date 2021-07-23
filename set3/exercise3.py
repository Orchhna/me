"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random
from typing_extensions import Type


def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    """
    while True:
        try:

            x = int(input(f"give a number between {low} and {high} "))
            if low <= x <= high:
                print("yep its a number")
                return x
            else:
                print(f" {x} is not between {low} and {high} ")

        except (ValueError, TypeError):
            print("error is not a number")


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

    print("\nWelcome to Orchi`s Guessing Game!")

    lowerBound = super_asker(-100, 100)
    upperBound = super_asker(lowerBound, 100)

    actualNumber = random.randint(lowerBound, upperBound)

    while True:
        print("Guess a number: ")
        guessedNumber = super_asker(lowerBound, upperBound)

        print(f"You guessed {guessedNumber}")

        if guessedNumber == actualNumber:
            print(f"Correct! It was {actualNumber}")
            return "You got it!"

        elif guessedNumber < actualNumber:
            print("Too small, try again 😢")
        elif guessedNumber > actualNumber:
            print("Too big, try again 🤔")
        else:
            print("something gone wrong")


if __name__ == "__main__":
    print(advancedGuessingGame())
