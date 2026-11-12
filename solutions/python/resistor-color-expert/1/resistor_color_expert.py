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
color_tolerance ={
    "grey" : "±0.05%",
    "violet" : "±0.1%",
    "blue" : "±0.25%",
    "green" : "±0.5%",
    "brown" : "±1%",
    "red" : "±2%",
    "gold" : "±5%",
    "silver" : "±10%"
}
def resistor_multiplier(resistor, multiplier_band):
    resistance = ""

    resistor_value = int(resistor) * (10 ** multiplier_band)
    
    if len(str(resistor_value)) > 9:
        resistance = str(resistor_value // (10 ** 9)) if resistor_value % (10 ** 9) == 0 else str(resistor_value / (10 ** 9))
        resistance += " gigaohms"
    elif 6 < len(str(resistor_value)) <= 9:
        resistance = str(resistor_value // (10 ** 6)) if resistor_value % (10 ** 6) == 0 else str(resistor_value / (10 ** 6))
        resistance += " megaohms"
    elif 3 < len(str(resistor_value)) <= 6:
        resistance = str(resistor_value // (10 ** 3)) if resistor_value % (10 ** 3) == 0 else str(resistor_value / (10 ** 3))
        resistance += " kiloohms"
    else:
        resistance = str(resistor_value) + " ohms" 

    return resistance


def resistor_label(colors):
    band_count = len(colors)
    resistor_label, resistance = "", ""
    
    if band_count == 1:
        resistor_label = str(color_codes[colors[0]]) + " ohms"

    if band_count == 4:
        # 2 bands are related to color codes
        # 3rd band is the multiplier
        # 4th band is the tolerance 
        resistance = resistor_multiplier(str(color_codes[colors[0]]) + str(color_codes[colors[1]]), color_codes[colors[2]])
        resistor_label = resistance + " " + color_tolerance[colors[3]]

    if band_count == 5:
        # 3 bands are related to color codes
        # 4th band is the multiplier
        # 5th band is the tolerance
        resistance = resistor_multiplier(str(color_codes[colors[0]]) + str(color_codes[colors[1]]) + str(color_codes[colors[2]]), color_codes[colors[3]])
        resistor_label = resistance + " " + color_tolerance[colors[4]]
            
    
    return resistor_label