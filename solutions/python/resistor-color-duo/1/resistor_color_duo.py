"""
    This script is for identifying color code of the given color combinations. 
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

def value(colors):
    """
        Identify the color code of the given color list.

        Paramaters:
            colors(list): String names of color.

        Return:
            int: Number codes of color list.
    """
    codes = str(color_codes[colors[0]]) + str(color_codes[colors[1]])

    return int(codes)