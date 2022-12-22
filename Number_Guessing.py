"""
This is the Number Guessing game made in Python
"""

from random import randint
from math import log2
from typing import Optional

def game() -> None:
    """
    The main game loop
    """

    # Ask user to input upper and lower bounds
    upper = check_valid_number(input("Please enter upper bound (positive integer): "), "upper")
    lower = check_valid_number(input("Please enter lower bound (positive intege): "), "lower")

    # Check if lower bound is larger than or equal to upper bound
    while lower >= upper:
        print("Lower bound should be smaller than upper bound!\n")
        upper = check_valid_number(input("Please enter upper bound (positive integer): "), "upper")
        lower = check_valid_number(input("Please enter lower bound (positive integer): "), "lower")

    # Generate an arbitrary number between upper and lower bounds
    answer = randint(lower, upper)

    # Use logarithm to calculate the chances of number guessing
    times = round(log2(upper - lower + 1))
    print(f"\nYou will have {times} chances to guess.\n")

    # Set an identifier for ending greeting and count
    win = False
    count = 1

    # Guessing loop
    while count <= times:

        # Print current round
        print_rounds(count)

        # Prompt the user to input a number between lower and upper bound
        number = check_valid_number(input(f"Please enter a number ({lower} ~ {upper}): "), "number", lower, upper)

        # Reply text with corresponding input
        if number == answer:
            print("You got the answer, congraz!!\n")
            win = True
            break
        if number > answer:
            print("You guessed too large, smaller~\n")
        else:
            print("You guessed too small, larger~\n")

        # Make sure the loop will be finite
        count += 1

    # Ending greeting
    print("Thanks for playing~\n" if win else "Time's up! You will do it better next time\n")

    # If the user want to continue then run the loop again
    if play_again():
        game()

def print_rounds(count: int) -> None:
    """
    Print out the current round of the game

    Parameters
    ----------
    count : int
        the current time of guessing

    Returns
    -------
    None
    """

    match count:
        case 1:
            print("< 1st Round >\n")
        case 2:
            print("< 2nd Round >\n")
        case 3:
            print("< 3rd Round >\n")
        case _:
            print(f"< {count}th Round> \n")

def check_type(types: str, lower: Optional[int] = None, upper: Optional[int] = None) -> str:
    """
    The function is used to check the types we want to input such as upper & lower bounds

    and number, then it will print corresponding prompt

    Parameters
    ----------
    types : str
        the input types such as upper & lower bounds and number
    lower: Optional[int] = None
        the lower bound
    upper: Optional[int] = None
        the upper bound

    Returns
    -------
    str
        The number input.
    """

    # New feature in Python 3.10
    match types:
        case "upper" | "lower":
            return input(f"Please enter {types} bound: ")

        # Check if the number is between upper and lower
        case "number":
            return input(f"Please enter a number ({lower} ~ {upper}): ")

def check_valid_number(num: str, types: str, lower: Optional[int] = None, upper: Optional[int] = None) -> int:
    """
    This function is used to check if the number is positive integer

    and assure that the input number is between the lower and upper bounds

    Parameters
    ----------
    num : str
        the input number
    types : str
        the input types such as upper & lower bounds and number
    lower: Optional[int] = None
        the lower bound
    upper: Optional[int] = None
        the upper bound

    Returns
    -------
    int
        The input number in integer type
    """

    # Use .isnumeric() to check if the number is positive integer 
    while not num.isnumeric():
        print("Wrong Input! Please enter again.\n")
        num = check_type(types, lower, upper)

    # Convert the number to an integer
    num = int(num)

    # If the input is for bounds we don't go following
    if not lower or not upper:
        return num

    # Prompt the user to enter another number if it is out of range
    if lower > num or num > upper:
        print("The number should be beween lower and upper.\n")
        num = check_valid_number(input(f"Please enter a number ({lower} ~ {upper}): "), types, lower, upper)

    # Return the integer type of number
    return num

# Ask if the user want to play again
def play_again() -> bool:
    """
    This function will ask and check if the user want to continue the game
    """

    check = input("Do you want to play again? (Y/N)")
    return check in ["Y", "y"]

if __name__ == "__main__":
    game()
