"""
    Identifying Resistor color and all colors code
"""
colors_dict = {
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

def color_code(color):
    """
        Identify the color code

        Parameters:
            color(str): Color name to be identify its code.

        Return:
            int: Number code of the color.
    """
    return colors_dict[color]


def colors():
    """
        Return all colors
    """
    return list(colors_dict.keys())
