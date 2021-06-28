"""Set 3, Exercise 2.

An example of how a guessing game might be written.
"""


import random


def exampleGuessingGame():
    """Play a game with the user.

    This is an example guessing game. It'll test as an example too.
    """
    print("\nWelcome to the guessing game!")  # print the title
    print("A number between 0 and _ ?")  # print the instruction
    upperBound = input(
        "Enter an upper bound: "
    )  # variable opperation that allows the user to put an input
    print(
        "OK then, a number between 0 and {} ?".format(upperBound)
    )  # print the question + format the above variable so the user can add an input
    upperBound = int(
        upperBound
    )  # the opperaton of int is to notice that a number is submitted

    actualNumber = random.randint(0, upperBound)  # computer select a random number

    guessed = False  # not sure if this line does anything

    while not guessed:
        guessedNumber = int(
            input("Guess a number: ")
        )  # instructs the user to input a number due to the operation int
        print(
            "You guessed {},".format(guessedNumber),
        )  # print a messeage combined with the input through the use of input
        if (
            guessedNumber == actualNumber
        ):  # condition 1: if the input matches the number of guessed number then excecute the body statement under
            print("You got it!! It was {}".format(actualNumber))
            guessed = True  # break the loop when the condition is equal to true and (return " you got it")
        elif (
            guessedNumber < actualNumber
        ):  # if the input number is bigger than the guessed number then excecute the body statement under
            print("Too small, try again :'(")
        else:
            print(
                "Too big, try again :'("
            )  # if the input number is smaller than the guessed number tha excecute the body statement under
    return "You got it!"


if __name__ == "__main__":
    exampleGuessingGame()
