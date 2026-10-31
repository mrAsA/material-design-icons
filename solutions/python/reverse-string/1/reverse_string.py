"""
    Reversing strings (reading them from right to left, rather than from left to right) is a surprisingly common task in programming.
"""
def reverse(text):
    """
        Reverse a given string.

        Some examples:
            Turn "stressed" into "desserts".
            Turn "strops" into "sports".
            Turn "racecar" into "racecar".

        Parameters:
            text(str): String to be reverse.

        Return:
            str: reverse string of given text.
    """
    text_array = tuple(text)

    return "".join(reversed(text_array))
