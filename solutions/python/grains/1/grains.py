"""
    Calculate grains by square and its total
"""

def square(number):
    """
        Calculate the square value based on number of squares in chessboard. There is total of 64 squares in a chessboard.

        Parameter:
            number(int): number of sqaure

        Return:
            int: Total grains on a given square
    """
    if number > 64 or number <= 0:
        raise ValueError("square must be between 1 and 64")

    grains_count = 1 if number == 1 else 2 ** (number - 1)

    return grains_count

def total():
    """
        Calculate the total grains in a chessboard. There is total of 64 squares in a chessboard.


        Return:
            int: Total grains on chessboard
    """
    return (2 ** 64) - 1
