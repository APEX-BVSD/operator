import pygame
from settings import *

evil_square: pygame.Rect = pygame.Rect(0,
                                       0,
                                       50, 50
 )

good_square: pygame.Rect = pygame.Rect(SCREEN_WIDTH-50,
                                       0,
                                       50, 50
 )

class UI():
    _clickable_objects: list = []
    _draggable_objects: list = [evil_square, good_square]
    _drawn_objects: list = [evil_square, good_square]
    _dragged_object = None


    def process_click(self, x, y):
        for object in self._draggable_objects:
            if x >= object.left and x <= object.right and y >= object.top and y <= object.bottom:
                self._dragged_object = object

    def process_ui(self, x, y):
        if self._dragged_object != None:
            self._dragged_object.top = y-25
            self._dragged_object.left = x-25

    def draw_objects(self, screen: pygame.Surface):  
        for object in self._drawn_objects:
            pygame.draw.rect(screen, (100,100,100), object)