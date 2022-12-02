from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost. 

    The responsibility of Score is to keep track of the points the player has earned by eating upgrade.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """

    def __init__(self, x=0, y=0, r=255, g=255, b=255):
        super().__init__(x, y, r, g, b)
        self._points = 0
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.

        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")
