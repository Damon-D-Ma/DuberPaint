import pygame
"""
Contains all the Shapes
"""


class Shape:
    """
    parent class for all Shapes
    """

    def __init__(self, top_left, bottom_right, colour, filled):
        """
        Constructor for a Shape

        Args:
            top_left (tuple): In the format of (x, y) for the top left corner
            bottom_right (tuple): In the format of (x, y) for the bottom right corner
            colour (tuple): In the format of (r, g, g) for the colour of the shape
            filled (boolean): Determines if the shape is filled with its set colour or not
        """
        self._top_left = top_left
        self._bottom_right = bottom_right
        self._colour = colour
        self._filled = filled

    def get_top_left(self):
        """
        returns the top left coordinate of the shape
        """
        return self._top_left

    def get_bottom_right(self):
        """
        returns the bottom right coordinate of the shape
        """
        return self._bottom_right
    
    def get_colour(self):
        """
        returns the colour of the rectangle
        """
        return self._colour
    
    def get_filled(self):
        """
        returns whether or not the shape is filled with its set colour or not
        """
        return self._filled


class Rectangle (Shape):
    """
    The Rectangle class
    Inherits from Shape
    """

    def draw(self, screen):
        """
        Draws the Rectangle

        Args:
            screen (pygame.Surface): the pygame Surface to draw a rectangle on
        """
        pygame.draw.rect(screen, self._colour, (self._top_left[0], self._top_left[1],
                                          abs(self._bottom_right[0] -
                                          self._top_left[0]),
                                          abs(self._bottom_right[1] - self._top_left[1])), self._filled)


class Ellipse (Shape):
    """
    The Ellipse class
    Inherits from Shape
    """

    def draw(self, screen):
        """
        Draws the Ellipse

        Args:
            screen (pygame.Surface): the pygame Surface to draw an Ellipse on
        """
        pygame.draw.ellipse(screen, self._colour, (self._top_left[0], self._top_left[1],
                                             abs(self._bottom_right[0] -
                                             self._top_left[0]),
                                             abs(self._bottom_right[1] - self._top_left[1])), self._filled)


class Line (Shape):
    """
    The Line class
    Inherits from Shape
    """


    def __init__(self, top_left, bottom_right, colour):
        """
        Constructor for the Line class
        
        Args:
            top_left (tuple): In the format of (x, y) for the top left corner
            bottom_right (tuple): In the format of (x, y) for the bottom right corner
            colour (tuple): In the format of (r, g, g) for the colour of the shape 
        """
        super().__init__(top_left, bottom_right, colour, True)


    def draw(self, screen):
        """
        Draws the Line

        Args:
            screen (pygame.Surface): the pygame surface the line will be drawed on
        """
        pygame.draw.line(screen, self._colour, (self._top_left), (self._bottom_right))
