import pygame
import brushes
from user import User
"""
Contains the components
"""


class DuberComponent:
    """
    Parent class for all DuberComponents
    """

    def __init__(self, x, y, width, height, colour):
        """
        DuberComponent constructor

        Args:
            x (int): the x position of the top left corner
            y (int): the y position of the top left corner
            width (int): the width of the rectangle the component is within
            height (int): the height of the rectangle the component is within
            colour (tuple): the colour to make it
        """
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._colour = colour

    def draw(self, screen):
        """
        Draws the DuberComponent on the screen

        Args:
            screen (pygame.surface): where to draw the component
        """
        pygame.draw.rect(
            screen,
            self._colour,
            (self._x,
             self._y,
             self._width,
             self._height),
            1)

    def selected(self, point):
        """
        Checks if the component has been selected

        Args:
            point (tuple): in the format of (x, y) for a point to check

        Returns:
            boolean: True if the component is selected, false otherwise
        """
        return self._x <= point[0] <= self._x + \
            self._width and self._y <= point[1] <= self._y + self._height


class DuberTextBox(DuberComponent):
    """
    The DuberComponent that can contain text
    """

    def __init__(self, x, y, width, height, colour, text, font, font_colour):
        """
        Constructor for the DuberTextBox

        Args:
            x (int): the x position of the top left corner of the component
            y (int): the y position of the top left corner of the component
            width (int): the width of the component
            height (int): the height of the component
            colour (tuple): the colour of the component
            text (string): the text within the component
            font (pygame.font): the font of which the text of the component uses
            font_colour (tuple): the colour of which the font of the text of the component is in
        """
        super().__init__(x, y, width, height, colour)
        self._text = text
        self._font = font
        self._font_colour = font_colour

    def draw(self, screen):
        """
        Draws the component on the screen

        Args:
            screen (pygame.surface): the surface to draw the component on
        """
        super().draw(screen)
        screen.blit(
            self._font.render(
                self._text,
                True,
                (self._font_colour)),
            (self._x + 5,
             self._y + 2))

    def get_text(self):
        """
        Gets the text in the DuberTextBox

        Returns:
            string: text in the DuberTextBox
        """
        return self._text

    def set_text(self, new_text):
        """
        Sets new_text as the text of the DuberTextComponent

        Args:
            new_text (string): the new text of the DuberTextComponent
        """
        self._text = new_text


class DuberColourButton(DuberComponent):
    """
    Button for setting colours
    """

    def __init__(self, x, y, colour):
        """
        Constructor of the DuberColourButton

        Args:
            x (int): the top left corner for the x position
            y (int): the top left corner's y position
            colour (tuple): the colour of the DuberColourButton
        """
        super().__init__(x, y, 20, 20, colour)

    def get_colour(self):
        """
        Gets the colour of the DuberColourButton

        Returns:
            tuple: the colour stored in the DuberColourComponent
        """
        return (self._colour)

    def set_colour(self, colour):
        """
        Sets a new colour for the DuberColourButton

        Args:
            colour (tuple): the new colour to give to the DuberColourButton
        """
        self._colour = colour

    def draw(self, screen):
        """
        Draws the component

        Args:
            screen (pygame.surface): The surface to draw the component on
        """
        pygame.draw.rect(
            screen,
            self._colour,
            (self._x,
             self._y,
             self._width,
             self._height))
        pygame.draw.rect(screen, (255, 255, 255),
                         (self._x, self._y, self._width, self._height), True)


class DuberBrushButton(DuberComponent):
    """
    Button for brush
    """

    def __init__(self, x, y, icon, brush):
        """
        Constructor for the DuberBrushButton

        Args:
            x (int): the x position of the top left corner
            y (int): the y position of the top left corner
            icon (pygame.image): the image icon
            brush (brushes.Brush): the brush that the button is storing

        """
        super().__init__(x, y, 32, 32, (128, 128, 128))
        self._icon = icon
        self._brush = brush

    def get_brush(self):
        """
        Reutnrs the brush stored in this button
        """
        return self._brush

    def set_brush(self, new_brush):
        """
        Sets a new brush

        Args:
            new_brush (brushes.Brush): the new brush to set
        """
        self._brush = new_brush

    def set_colour(self, new_colour):
        """
        Sets the colour of the brush
            new_colour (tuple): the new colour of the brush in the button
        """
        self._brush.set_colour(new_colour)

    def set_icon(self, new_icon):
        """
        Sets a new icon

        Args:
            new_icon (pygame.image): the new image to set
        """
        self._icon = new_icon

    def draw(self, screen):
        """
        Draws the component on the screen

        Args:
            screen (pygame.surface): the surface to draw the component on
        """
        pygame.draw.rect(
            screen,
            self._colour,
            (self._x,
             self._y,
             self._width,
             self._height),
            0)
        if not isinstance(self._brush, brushes.Eraser):
            pygame.draw.rect(screen, self._brush.get_colour(),
                             (self._x, self._y, 8, 8), 0)
            pygame.draw.rect(screen, (0, 0, 0), (self._x, self._y, 8, 8), 1)

        screen.blit(self._icon, (self._x, self._y))


class DuberShapeButton(DuberComponent):
    """
    Button for shapes
    """

    def __init__(self, x, y, icon, shape_colour):
        """
        Constructor for the DuberShapeButton

        Args:
            x (int): the x position of the top left corner
            y (int): the y position of the top left corner
            icon (pygame.image): the image icon
            colour (tuple): the rgb colour value of the shape stored in the button
        """
        super().__init__(x, y, 75, 75, (255, 255, 255))
        self._icon = icon
        self._shape_colour = shape_colour

    def get_shape_colour(self):
        """
        Gets the colour of the shape from the button
        """
        return self._shape_colour

    def set_shape_colour(self, new_colour):
        """
        Sets a new colour for the shape in the button

        Args:
            new_colour (tuple): the RGB value of the new colour
        """
        self._shape_colour = new_colour

    def draw(self, screen):
        """
        Draws the component on the screen

        Args:
            screen (pygame.surface): the surface to draw the component on
        """
        pygame.draw.rect(
            screen,
            self._colour,
            (self._x,
             self._y,
             self._width,
             self._height),
            0)
        pygame.draw.rect(screen, self._shape_colour,
                         (self._x, self._y, 12, 12), 0)
        pygame.draw.rect(screen, (0, 0, 0), (self._x, self._y, 12, 12), 1)
        screen.blit(self._icon, (self._x, self._y))


class DuberUserButton(DuberComponent):
    """
    A button to select users in the board in the main window
    """

    def __init__(self, x, y, empty, font, user):
        """
        Constructor for the user button

        Args:
            x (int): the x position of the top left corner
            y (int): the y position of the top left corner
            empty (boolean): determines if this button is storing a user or not (since the room might not be full)
            font (pygame.font): the font of the button
            user (user.User): The user that is stored in the button
        """
        self._empty = empty
        self._font = font
        self._user = user
        super().__init__(x, y, 160, 40, (128, 128, 128))

    def set_user(self, new_user):
        """
        Assigns a new user to this button

        Args:
            new_user (user.User): The new user to be assigned to this button
        """
        self._user = new_user

    def get_user(self):
        """
        Returns the user assigned to this button
        """
        return self._user

    def check_if_empty(self):
        """
        Returns whether or not there is a user assigned to this button
        """
        return self._empty

    def set_empty(self, empty):
        """
        Changes the status of if the user is assigned to this button
        """
        self._empty = empty

    def toggle_empty(self):
        """
        Toggles the status of if the user is assigned to this button
        """
        self._empty = not self._empty

    def draw(self, screen):
        """
        Draws the button on the given window

        Args:
            screen (pygame.surface): the window that the button will be drawn on
        """
        pygame.draw.rect(
            screen,
            self._colour,
            (self._x,
             self._y,
             self._width,
             self._height),
            1)
        screen.blit(self._font.render(self._user.get_username(),
                    True, (255, 255, 255)), (self._x, self._y))
