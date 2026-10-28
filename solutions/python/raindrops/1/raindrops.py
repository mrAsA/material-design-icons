"""
    Raindrops is a slightly more complex version of the FizzBuzz challenge, a classic interview question.
    If a given number:

    is divisible by 3, add "Pling" to the result.
    is divisible by 5, add "Plang" to the result.
    is divisible by 7, add "Plong" to the result.
    is not divisible by 3, 5, or 7, the result should be the number as a string.

"""
def convert(number):
    """
        Convert the number into a Raindrops.

        Parameters:
            number(int): To identify what the sound of raindrop.

        Return:
            str: The sound of the Raindrop.
    """
    raindrop = ""

    if number % 3 == 0:
        raindrop += "Pling"
        
    if number % 5 == 0:
        raindrop += "Plang"
        
    if number % 7 == 0:
        raindrop += "Plong"
    
    if not raindrop:
        raindrop += str(number)

    return raindrop
