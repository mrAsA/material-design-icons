handshake_codes = {
    1 : "wink",
    2 : "double blink",
    4 : "close your eyes",
    8 : "jump",
    16 : "Reverse the order of the operations in the secret handshake."
}
def commands(binary_str):
    secret_handshake = []
    
    for index_code, code in enumerate(reversed(list(binary_str))):
        if code == "1" and index_code == 4:
            secret_handshake = reversed(secret_handshake)
        elif code == "1" :
            secret_handshake.append(handshake_codes[2 ** int(index_code)])

        

    return list(secret_handshake)

    