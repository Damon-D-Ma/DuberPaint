"""
Contains all valid brushes
"""

import shapes
import pygame


class Brush:
    """
    Brush class
    """

    def __init__(self, colour, width):
        """
        Constructor, assigns values

        Args:
            colour (tuple): RGB values for the brush colour
            width (int): width of brush
        """
        self._colour = colour
        self._width = width

    def make_brush_stroke(self, position):
        """
        Creates a brush stroke when the brush is used

        Args:
            position (tuple): the coordinates that the brush is on to make the mark
        """
        return BrushStroke(self._colour, self._width, position)

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

    def __init__(self, width):
        """
        Eraser constructor

        Args:
            width (int): width of eraser
            height (int): height of eraser
        """
        super().__init__((255, 255, 255), width)


class BrushStroke(Brush, shapes.Shape):
    """
    The mark that the Brush class would make on the canvas
    """

    def __init__(self, colour, width, coordinates):
        """
        Constructor for the BrushStroke

        Args:
            colour (tuple): the RGB value of the brush mark
            width (int): the width of the mark
            height (int): the height of the mark
            coordinates (tuple): the position of the mark on the brush'es canvas
        """
        super().__init__(colour, width)
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

        pygame.draw.circle(
            screen,
            self._colour,
            self._coordinates,
            (int(self._width / 2)),
            0)

    def mark(self, canvas):
        """
        Marks the brushstroke on the canvas

        Args:
            canvas (list): 3d array keeping track of each pixel on the board

        Returns:
            list: the updated canvas
        """
        for x in range(self._coordinates[0] - self._width, self._coordinates[0] + self._width):
            for y in range(self._coordinates[1] - self._width, self._coordinates[1] + self._width):
                if (((x - self._coordinates[0])*(x - self._coordinates[0])) + ((y - self._coordinates[1])*(y - self._coordinates[1]))) < (self._width * self._width):
                    canvas[y - 115][x - 200] = self._colour
        return canvas

def fill(canvas, point, colour):
    """
    Fills an area of the canvas

    Args:
        canvas (list): the canvsa to fill something on
        point (tuple): the point to start filling at
        colour (list): the colour to fill with

    Returns:
        list: the newly filled canvas
    """
    original_colour = canvas[point[0]][point[1]]
    mock_queue = []
    mock_queue.append(point)
    while len(mock_queue) > 0:
        new_point = mock_queue.pop(0)
        canvas[new_point[0]][new_point[1]] = colour
        if (new_point[0] + 1 < len(canvas)) and (canvas[new_point[0] + 1]
                                                 [new_point[1]] == original_colour):
            mock_queue.append((new_point[0] + 1, new_point[1]))
        if (new_point[0] - 1 >= 0) and (canvas[new_point[0] - 1]
                                        [new_point[1]] == original_colour):
            mock_queue.append((new_point[0] - 1, new_point[1]))
        if (new_point[1] + 1 < len(canvas[0])) and (canvas[new_point[0]]
                                                    [new_point[1] + 1] == original_colour):
            mock_queue.append((new_point[0], new_point[1] + 1))
        if (new_point[1] + 1 >= 0) and (canvas[new_point[0]]
                                        [new_point[1] - 1] == original_colour):
            mock_queue.append((new_point[0], new_point[1] - 1))
    return canvas
