"""
    The Collatz Conjecture, a puzzle that has baffled thinkers for decades.
    The rules were deceptively simple. Pick any positive integer.
    
        If it's even, divide it by 2.
        If it's odd, multiply it by 3 and add 1.
    
    Then, repeat these steps with the result, continuing indefinitely.
    
    Curious, you picked number 12 to test and began the journey:
    
    12 ➜ 6 ➜ 3 ➜ 10 ➜ 5 ➜ 16 ➜ 8 ➜ 4 ➜ 2 ➜ 1
"""

def steps(number):
    """
        Count the steps of number to 1 using collatz conjecture

        Parameters:
            number(int): number to be run in collatz conjecture

        Return:
            int: total steps need in collatz conjecture
    """
    if number <= 0:
        # example when argument is zero or a negative integer
        raise ValueError("Only positive integers are allowed")

    count = 0

    while number > 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = (number * 3) + 1

        count += 1

    return count
    
