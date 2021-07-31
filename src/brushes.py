"""
Contains all valid brushes
"""

import shapes
import pygame

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
        self._colour = colour
        self._width = width
        self._height = height


        def get_colour(self):
            """
            returns the colour of the brush
            """
            return self._colour

        def get_width(self):
            """
            returns the width of the brush
            """
            return self._width

        def set_colour(self, new_colour):
            """
            sets the colour of the brush
            
            args:
                new_colour (tuple): the new colour of the brush in RGB
            """
            self._colour = new_colour

        def set_width(self, new_width):
            """
            sets the width of the brush

            args:
                new_wdith (int): the new width of the brush
            """
            self._width = new_width




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

class BrushStroke(Brush, shapes.Shape):
    """
    The mark that the Brush class would make on the canvas
    """

    def __init__(self, colour, width, height, coordinates):
        """
        Constructor for the BrushStroke

        Args:
            colour (tuple): the RGB value of the brush mark
            width (int): the width of the mark
            height (int): the height of the mark
            coordinates (tuple): the position of the mark on the brush'es canvas
        """
        super.__init__(colour, width, height)
        self._coordinates = coordinates

    def get_coordinates(self):
        """
        returns the mark's position
        """
        return self._coordinates

    def draw(self, screen):
        """
        Draws the brush mark on the canvas

        Args:
            screen (pygame.surface): the pygame surface the brush mark will be drawn on
        """

        pygame.draw.circle(screen, self._colour, self._coordinates, (self._width/2), 0)
