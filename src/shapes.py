import pygame
"""
Contains all the Shapes
"""


class Shape:
    """
    parent class for all Shapes
    """

    def __init__(self, top_left, bottom_right):
        """
        Constructor for a Shape

        Args:
            top_left (tuple): In the format of (x, y) for the top left corner
            bottom_right (tuple): In the format of (x, y) for the bottom right corner
        """
        self.top_left = top_left
        self.bottom_right = bottom_right


class Rectangle (Shape):
    """
    The Rectangle class
    Inherits from Shape
    """

    def draw(self, screen, colour, filled):
        """
        Draws the Rectangle

        Args:
            screen (pygame.Surface): the pygame Surface to draw a rectangle on
            colour (pygame.Color): the Color (r, g, b) to make the rectangle
            filled (boolean): whether or not the rectangle is filled
        """
        pygame.draw.rect(screen, colour, (self.top_left[0], self.top_left[1],
                                          self.bottom_right[0] -
                                          self.top_left[0],
                                          self.bottom_right[1] - self.top_left[1]), filled)


class Ellipse (Shape):
    """
    The Ellipse class
    Inherits from Shape
    """

    def draw(self, screen, colour, filled):
        """
        Draws the Ellipse

        Args:
            screen (pygame.Surface): the pygame Surface to draw an Ellipse on
            colour (pygame.Color): the Color (r, g, b) to make the Ellipse
            filled (boolean): whether or not the Ellipse is filled
        """
        pygame.draw.ellipse(screen, colour, (self.top_left[0], self.top_left[1],
                                             self.bottom_right[0] -
                                             self.top_left[0],
                                             self.bottom_right[1] - self.top_left[1]), filled)
