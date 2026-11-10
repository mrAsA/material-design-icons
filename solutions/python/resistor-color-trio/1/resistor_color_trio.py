"""
    Resistor Part 3
"""
color_codes = {
    "black": 0, 
    "brown": 1, 
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}
metrics = {
    3: "Kilohms",
    6: "Megaohms",
    9: "Gigaohms"
}
def label(colors):
    """
        In Resistor Color Duo you decoded the first two colors. 
        For instance: orange-orange got the main value 33. 
        The third color stands for how many zeros need to be added to the main value. 
        The main value plus the zeros gives us a value in ohms. 
        For the exercise it doesn't matter what ohms really are. For example:
    
        orange-orange-black would be 33 and no zeros, which becomes 33 ohms.
        orange-orange-red would be 33 and 2 zeros, which becomes 3300 ohms.
        orange-orange-orange would be 33 and 3 zeros, which becomes 33000 ohms.

        10 ** 3 = 1 000 ohms = 1 Kilohms
        10 ** 6 = 1 000 000 ohms = 1 Megaohms
        10 ** 9 = 1 000 000 000 ohms = Gigaohms
        Parameters:
            colors(str): String color names to be transalated in codes

        Return:
            str: color codes values.
    """
    resistor_label = ""
    count, color_value, tot_resistor, color_code = 0, 0, 0, 0
    
    while count < 3:
        color_code = color_codes[colors[count]]
        
        if count == 2:
            tot_resistor = 10 ** color_code
            color_value = int(resistor_label) * tot_resistor
        else:
            resistor_label += str(color_code) 
        
        count += 1

    if str(color_value).count("0") >= 9:
        resistor_label = str(color_value // (10 ** 9)) + " gigaohms"
    elif 6 <= str(color_value).count("0") < 9:
        resistor_label = str(color_value // (10 ** 6)) + " megaohms"
    elif 3 <= str(color_value).count("0") < 6:
        resistor_label = str(color_value // (10 ** 3)) + " kiloohms"
    else:
        resistor_label = str(color_value) + " ohms"
        
    return resistor_label
