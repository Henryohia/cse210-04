#shane
import pyray
from game.shared.point import Point
"""
The above comment will be updated when the 'shared' folder is complete
"""

class KeyboardService:
    """
    Detects the player's input on the arrow keys

    The input is then translated into a point representing direction

    Attributes:
        cell_size (int): For scaling directional input to a grid
    """

    def __init__(self, cell_size = 1) -> None:

        """
        Constructs an new KeyboardService using the specified cell size

        Args:
            cell_size (int): The size of a cell in the display grid
        """

        self._cell_size = cell_size

    def get_direction(self):

        """
        Gets the selected direction based on the currently pressed keys

        Returns:
            Point: The selected direction
        """

        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1

        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1

        if pyray.is_key_down(pyray.KEY_UP):
             dy = -1

        if pyray.is_key_down(pyray.KEY_DOWN):
             dy = 1

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)

        return direction