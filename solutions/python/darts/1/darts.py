"""
    Calculate the points scored in a single toss of a Darts game.
    Darts is a game where players throw darts at a target.
    In our particular instance of the game, the target rewards 4 different amounts of points, depending on where the dart lands:
        If the dart lands outside the target, player earns no points (0 points).
        If the dart lands in the outer circle of the target, player earns 1 point.
        If the dart lands in the middle circle of the target, player earns 5 points.
        If the dart lands in the inner circle of the target, player earns 10 points.
"""
def score(x, y):
    """
        Define the score base on the coordinates

        Parameters:
            x(int): value of x.
            y(int): value of y.

        Return:
            int: The score based on coordinates it landed.
    """
    dart_info = {1: 10, 5: 5, 10: 1}

    radius = (x ** 2 + y ** 2) ** 0.5
    #  This is my newbie approach
    #score = 0
    
    #for key, point in dart_info.items():
    #    if radius <= key:
    #        score = point
    #        break

    score = [point for key, point in dart_info.items() if radius <= key]
    
    return (score[0] if score else 0)
