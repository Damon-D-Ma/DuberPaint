"""
Contains all valid brushes
"""


class Brush:
    """
    Brush class
    """

    def __init__(self, colour, width, height):
        """
        Constructor, assigns values

        Args:
            colour (tuple): RGB values for the brush colour
            width (int): width of brush
            height (int): height of brush
        """
        self.colour = colour
        self.width = width
        self.height = height


class Eraser(Brush):
    """
    Eraser, inherits from Brush
    """

    def __init__(self, width, height):
        """
        Eraser constructor

        Args:
            width (int): width of eraser
            height (int): height of eraser
        """
        super.__init__((255, 255, 255), width, height)
