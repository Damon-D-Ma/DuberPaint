import pygame
from math import sqrt
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

        Returns:
            tuple: the coordinates of the top left
        """
        return self._top_left

    def get_bottom_right(self):
        """
        returns the bottom right coordinate of the shape

        Returns:
            tuple: the coordinates of the bottom right
        """
        return self._bottom_right

    def get_colour(self):
        """
        returns the colour of the shape

        Returns:
            list: [r, g, b] of the colour of the shape
        """
        colour_list = [self._colour[0], self._colour[1], self._colour[2]]
        return colour_list

    def get_filled(self):
        """
        returns whether or not the shape is filled with its set colour or not

        Returns:
            boolean: if the shape is filled or not
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

    def mark(self, canvas):
        """
        Marks the rectangle on the canvas

        Args:
            canvas (list): surface to mark

        Returns:
            (list): the canvas but marked
        """
        for i in range(self._top_left[0] - 200, self._bottom_right[0] - 200):
            # mark horizontals
            canvas[self._top_left[1] - 115][i] = self.get_colour()
            canvas[self._bottom_right[1] - 115][i] = self.get_colour()
        for i in range(self._top_left[1] - 115, self._bottom_right[1] - 115):
            # mark verticals
            canvas[i][self._top_left[0] - 200] = self.get_colour()
            canvas[i][self._bottom_right[0] - 200] = self.get_colour()
        return canvas


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
        if (abs(self._bottom_right[0] - self._top_left[0]) > 1) and (abs(self._bottom_right[1] - self._top_left[1]) > 1):
            pygame.draw.ellipse(screen, self._colour, (self._top_left[0], self._top_left[1],
                                                   abs(self._bottom_right[0] -
                                                       self._top_left[0]),
                                                   abs(self._bottom_right[1] - self._top_left[1])), self._filled)

    def mark(self, canvas):
        """
        Marks the ellipse on the canvas using math

        Args:
            canvas (list): the canvas to mark the ellipse on

        Returns:
            list: the newly marked canvas
        """
        a = (self._bottom_right[0] - self._top_left[0]) / 2.0
        b = (self._bottom_right[1] - self._top_left[1]) / 2.0
        if (a > 0) and (b > 0):
            h = (self._top_left[0] + self._bottom_right[0]) / 2.0
            k = (self._top_left[1] + self._bottom_right[1]) / 2.0
            for x in range(self._top_left[0], self._bottom_right[0] + 1):
                # derived from the ellipse formula
                y1 = round(
                    sqrt((b * b) * (1 - (((x - h) * (x - h)) / (a * a)))) + k)
                y2 = round(-sqrt((b * b) * (1 - (((x - h) * (x - h)) / (a * a)))) + k)

                canvas[y1 - 115][x - 200] = self.get_colour()
                canvas[y2 - 115][x - 200] = self.get_colour()

            for y in range(self._top_left[1], self._bottom_right[1] + 1):
                x1 = round(
                    sqrt((a * a) * (1 - (((y - k) * (y - k)) / (b * b)))) + h)
                x2 = round(-sqrt((a * a) * (1 - (((y - k) * (y - k)) / (b * b)))) + h)

                canvas[y - 115][x1 - 200] = self.get_colour()
                canvas[y - 115][x2 - 200] = self.get_colour()

        return canvas


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
        pygame.draw.line(
            screen,
            self._colour,
            (self._top_left),
            (self._bottom_right))

    def mark(self, canvas):
        """
        Marks the line on the screen

        Args:
            canvas (pygame.surface): The surface to mark the line on

        Returns:
            list: the newly marked canvas
        """
        if (self.get_top_left()[0] - self.get_bottom_right()[0]) == 0:
            m = 99999999
        else:
            m = (self.get_top_left()[1] - self.get_bottom_right()[1]) / \
                (self.get_top_left()[0] - self.get_bottom_right()[0])
        b = self.get_bottom_right()[1] - m * self.get_bottom_right()[0]
        for i in range(self.get_top_left()[0], self.get_bottom_right()[0] + 1):
            canvas[int(m * i + b) - 115][i - 200] = self.get_colour()
        for i in range(self.get_bottom_right()[0], self.get_top_left()[0] + 1):
            canvas[int(m * i + b) - 115][i - 200] = self.get_colour()
        return canvas
