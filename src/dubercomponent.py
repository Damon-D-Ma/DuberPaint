import pygame
"""
Contains the components
"""

class DuberComponent:
    def __init__(self, x, y, width, height, colour):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._colour = colour

    def draw(self, screen):
        pygame.draw.rect(screen, self._colour, (self._x, self._y, self._width, self._height), 1)

    def selected(self, point):
        # point is a tuple because pygame mouse takes in a tuple
        return self._x <= point[0] <= self._x + self._width and self._y <= point[1] <= self._y + self._height

class DuberTextBox(DuberComponent):
    def __init__(self, x, y, width, height, colour, text, font, font_colour):
        super().__init__(x, y, width, height, colour)
        self._text = text
        self._font = font
        self._font_colour = font_colour

    def draw(self, screen):
        super().draw(screen)
        screen.blit(self._font.render(self._text, True, (self._font_colour)), (self._x, self._y))

    def get_text(self):
        return self._text
    
    def set_text(self, new_text):
        self._text = new_text

class DuberColourButton(DuberComponent):
    def __init__(self, x, y, colour):
        super().__init__(self,x,y,32,32,colour)

    def get_colour(self):
        return(self._colour)
    
    def set_colour(self, colour):
        self._colour = colour

    def draw(self, screen):
        pygame.draw.rect(screen, self._colour, (self._x, self._y, self._width, self._height))


class DuberBrushButton(DuberComponent):
    def __init__(self, x,y, icon):
        super().__init__(self,x,y,32,32,(0,0,0))
        self._icon = icon

    def set_icon(self, new_icon):
        self._icon = new_icon
    
    def draw(self, screen):
        screen.blit(self._icon, (self._x, self._y))

