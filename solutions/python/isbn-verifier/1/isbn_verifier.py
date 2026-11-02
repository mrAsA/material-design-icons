"""
    The ISBN-10 verification process is used to validate book identification numbers.
"""
def is_valid(isbn):
    """
        The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only). 
        In the case the check character is an X, this represents the value '10'. 
        These may be communicated with or without hyphens, and can be checked for their validity by the following formula:
            (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
        If the result is 0, then it is a valid ISBN-10, otherwise it is invalid.

        Parameters:
            isbn(str): ISBN string aplhanumerals to be check.

        Return:
            bool: if the ISBN is a valid and false if not.
    """
    digits = list(isbn.replace("-",""))
    check, isbn, count = 0, 0, 10

    if len(digits) < 10 or len(digits) > 10:
        return False
    
    if not digits[9].isdigit() and digits[9] == "X":
          digits[9] = "10"
    elif not digits[9].isdigit():
        return False

    while count > 0:
        if not digits[10 - count].isdigit():
            return False
            
        isbn += int(digits[10 - count]) * count
        count -= 1

    return (isbn % 11 == 0)
        
        
