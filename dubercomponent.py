import pygame
"""
Contains the components
"""

class DuberComponent:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class DuberTextBox:
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.text = ""

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height), 1)

    def selected(self, point):
        # point is a tuple because pygame mouse takes in a tuple
        return self.x <= point[0] <= self.x + self.width and self.y <= point[1] <= self.y + self.height