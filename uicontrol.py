import pygame
from settings import *

evil_square: pygame.Rect = pygame.Rect(0,
                                       0,
                                       300, 300
 )


image: pygame.Surface = pygame.image.load("Untitled.png")

class UI():
    _clickable_objects: list = []
    _draggable_objects: list = [evil_square]
    _drawn_objects: list = []
    _dragged_object: pygame.Surface = None

    def process_click(self, x, y):
        for object in self._draggable_objects:
            if x >= object.left and x <= object.right and y >= object.top and y <= object.bottom:
                self._dragged_object = object
                pygame.Surface.set_alpha(self._dragged_object, 50)

    def process_ui(self, x, y):
        if self._dragged_object != None:
            self._dragged_object.left = x - (pygame.Surface.get_width(self._dragged_object) / 2)
            self._dragged_object.top = y - (pygame.Surface.get_height(self._dragged_object) / 2)
            

    def draw_objects(self, screen: pygame.Surface):  
        for object in self._drawn_objects:
            screen.blit(object, (object.topleft))
        if self._dragged_object != None:
            screen.blit(self._dragged_object, (self._dragged_object.topleft))