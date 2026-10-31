"""
    Pangram comes from Greek, παν γράμμα, pan gramma, which means "every letter".
"""
def is_pangram(sentence):
    """
        Pangram comes from Greek, παν γράμμα, pan gramma, which means "every letter".
        
        The best known English pangram is:
            The quick brown fox jumps over the lazy dog.

        Parameters:
            sentence(str): String to be check if it is a pangram.

        Return:
            boolean: True if it is a pangram and false otherwise
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    return set(alphabet).issubset(set(sentence.lower()))
    