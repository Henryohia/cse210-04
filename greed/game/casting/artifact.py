import random
from game.casting.actor import Actor
from game.shared.point import Point

class Artifact(Actor):
    """A visible, moveable thing that participates in the game. 
    
    The responsibility of Artifact is to keep track of keep track of its kind, its value, and its visibility

    Attributes:
        _kind (string): The text that represents its kind
        _value (int): The value it worths
        _is_visible (boolean): if it is visible or not.
        _velocity_factor (int): The factor that would affect the velocity
        _message (string): message for the artifact
    """

    def __init__(self):
        """Constructs a new Artifact using parent's constructor"""
        super().__init__()
        self._kind = "A normal one"
        self._value = 1
        self._is_visible = True
        self._velocity_factor = 15
        self._message = ""


    def get_message(self):
        """Gets the artifact's message.

        Returns:
            string: The message.
        """
        return self._message

    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message

    def get_kind(self):
        """Gets the artifact's kind.
        
        Returns:
            String: The artifact's text that represents its kind.
        """
        return self._kind

    def get_value(self):
        """Gets the artifact's value.
        
        Returns:
            integer: The artifact's value.
        """
        return self._value

    def get_visibility(self):
        """Gets the artifact's visibility.
        
        Returns:
            boolean: if the artifact is visible.
        """
        return self._is_visible

    def set_kind(self, kind):
        """Updates the kind to the given one.
        
        Args:
            kind (String): The given kind.
        """
        self._kind = kind

    def set_value(self, value):
        """Updates the value to the given one.
        
        Args:
            value (integer): The given value.
        """
        self._value = value
    
    def set_visibility(self, is_visible):
        """Updates the visibility to the given one.
        
        Args:
            is_visible (boolean): The given visibility.
        """
        self._is_visible = is_visible

    def set_velocity_factor(self, velocity_factor):
        """Updates the velocity factor to the given one.
        
        Args:
            velocity_factor (integer): The given velocity_factor.
        """
        self._velocity_factor = velocity_factor

    def move_down(self):
        """Moves the artifact one place down. 
        """
        direction = Point(0, 1)
        velocity = direction.scale(self._velocity_factor)
        self._velocity = velocity
        x = self._position.get_x()
        y = self._position.get_y() + self._velocity.get_y()
        self._position = Point(x, y)

    def set_random_position(self, cell_size, max_x, max_y):
        """Sets a random position to an artifact.
        
        Args:
            size (integer): The cell size.
            cols (integer): The total columns for the window.
            rows (integer): The total rows for the window.
        """
        cols = int(max_x / cell_size)
        rows = int(max_y / cell_size)
        x = random.randint(1, cols - 1)
        y = random.randint(- rows + 1, 1)
        position = Point(x, y)
        position = position.scale(cell_size)
        self._position = position
