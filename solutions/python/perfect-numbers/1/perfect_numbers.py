"""
    Determine if a number is perfect, abundant, or deficient based on Nicomachus' (60 - 120 CE) classification scheme for positive integers.
"""
def classify(number):
    """ 
        The Greek mathematician Nicomachus devised a classification scheme for positive integers, identifying each as belonging uniquely to the categories of perfect, abundant, or deficient based on their aliquot sum. 
        The aliquot sum is defined as the sum of the factors of a number not including the number itself. 
        For example, the aliquot sum of 15 is 1 + 3 + 5 = 9.

        Parameters:
            number(int): the number you will check for its aliquot sum.

        Return:
            str: The classifacation of the number given based on aliquot sum
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")


    #  my simple approach
    #aliquot = 0
    #for count in range(1,number):
    #    if number % count == 0:
    #        aliquot += count

    category = ""
    factors = [count for count in range(1, number) if number % count == 0]

    if number == sum(factors):
        category = "perfect"
    elif number < sum(factors):
        category = "abundant"
    elif number > sum(factors):
        category = "deficient"

    return category