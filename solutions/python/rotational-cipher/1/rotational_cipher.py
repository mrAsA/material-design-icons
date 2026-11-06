"""
    The Caesar cipher is a simple shift cipher that relies on transposing all the letters in the alphabet using an integer key between 0 and 26. 
    Using a key of 0 or 26 will always yield the same output due to modular arithmetic. 
    The letter is shifted for as many values as the value of the key.
"""
def rotate(text, key):
    """
        The general notation for rotational ciphers is ROT + <key>. The most commonly used rotational cipher is ROT13.
        A ROT13 on the Latin alphabet would be as follows:
            Plain:  abcdefghijklmnopqrstuvwxyz
            Cipher: nopqrstuvwxyzabcdefghijklm

        Parameters:
            text(str): String will use to be cipher.
            key(int): Number of letter to be cipher.

        Return:
            str: Ciphered String by given key.
    """
    from string import ascii_lowercase, ascii_uppercase

    lowercase_list = list(ascii_lowercase)
    uppercase_list = list(ascii_uppercase)
    text_list = list(text)

    #  identify if the key is in range of alphabet
    new_key = key if key < 26 else key % 26

    #  enumerate the list text to get the index and the character to cipher
    for char_index, character in enumerate(text_list):

        #  identify if the character is in aplhabet
        if character in lowercase_list or character in uppercase_list:
            #  identify the index of the character in the alphabet
            alp_index = next(letter_index for letter_index, letter in enumerate(lowercase_list) if character.lower() == letter)
            
            #  change the character based on key given
            cipher_index = new_key + alp_index if (new_key + alp_index) < 26 else (new_key + alp_index) % 26
            text_list[char_index] = lowercase_list[cipher_index] if character.islower() else uppercase_list[cipher_index]


    return "".join(text_list)


                
                