import pygame
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
        pygame.draw.rect(screen, self._colour, (self._x, self._y, self._width, self._height), 1)

    def selected(self, point):
        """
        Checks if the component has been selected

        Args:
            point (tuple): in the format of (x, y) for a point to check

        Returns:
            boolean: True if the component is selected, false otherwise
        """
        return self._x <= point[0] <= self._x + self._width and self._y <= point[1] <= self._y + self._height

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
        screen.blit(self._font.render(self._text, True, (self._font_colour)), (self._x +5, self._y +2))

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
        super().__init__(self,x,y,32,32,colour)

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
        super().draw(screen)
        pygame.draw.rect(screen, self._colour, (self._x, self._y, self._width, self._height))


class DuberBrushButton(DuberComponent):
    """
    Button for brush
    """
    def __init__(self, x,y, icon):
        """
        Constructor for the DuberBrushButton

        Args:
            x (int): the x position of the top left corner
            y (int): the y position of the top left corner
            icon (pygame.image): the image icon
        """
        super().__init__(self,x,y,32,32,(0,0,0))
        self._icon = icon

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
        super().draw(screen)
        screen.blit(self._icon, (self._x, self._y))

