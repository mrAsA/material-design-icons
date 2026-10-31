"""
    An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.
"""
def is_isogram(phrase):
    """
        Examples of isograms:
            lumberjacks
            background
            downstream
            six-year-old
        
        The word isograms, however, is not an isogram, because the s repeats.

        Parameters:
            phrase(str): String to be check if it is an isogram.

        Return:
            bool: True if it is an isogram else False otherwise.
    """
    from string import ascii_lowercase

    chars = tuple(phrase.lower())

    for char in set(chars):
        if char in ascii_lowercase:
            if chars.count(char) > 1:
                return False

    return True
            
            
    
    
