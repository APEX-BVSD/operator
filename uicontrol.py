import pygame
from settings import *
from objects import *
import pygame
from settings import *


class UI():
    _clickable_objects: list = []
    _draggable_objects: list = [placeholder]
    _drawn_objects: list = [placeholder]
    _dragged_object = None
    _dragged_x: int = 0
    _dragged_y: int = 0

    def process_click(self, x, y):
        for object in self._draggable_objects:
            if x >= object.hitbox.left and x <= object.hitbox.right and y >= object.hitbox.top and y <= object.hitbox.bottom:
                self._dragged_object = object
                

    def process_ui(self, x, y):
        if self._dragged_object != None:
            self._dragged_object.hitbox.left = x - (self._dragged_object.hitbox.width / 2)
            self._dragged_object.hitbox.top = y - (self._dragged_object.hitbox.height / 2)

    def draw_objects(self, screen: pygame.Surface):  
        for object in self._drawn_objects:
            screen.blit(object.image, object.hitbox)
        if self._dragged_object != None:
            screen.blit(self._dragged_object.image, (self._dragged_x, self._dragged_y))