import pygame
from settings import *
from objects import *
import pygame
from settings import *

placeholder: Placeholder = Placeholder

class UI():
    _clickable_objects: list = []
    _draggable_objects: list = [placeholder]
    _drawn_objects: list = [placeholder]
    _dragged_object = None
    _dragged_sprite = None
    _dragged_x: int = 0
    _dragged_y: int = 0

    def process_click(self, x, y):
        for object in self._draggable_objects:
            if x >= object.hitbox.left and x <= object.hitbox.right and y >= object.hitbox.top and y <= object.hitbox.bottom:
                self._dragged_object = object
                self._dragged_sprite = pygame.Surface.copy(object.image)
                pygame.Surface.set_alpha(self._dragged_sprite, 50)
                

    def process_ui(self, x, y):
        if self._dragged_object != None:
            self._dragged_x = x - (self._dragged_object.hitbox.width / 2)
            self._dragged_y = y - (self._dragged_object.hitbox.height / 2)

    def draw_objects(self, screen: pygame.Surface):  
        for object in self._drawn_objects:
            screen.blit(object.image, object.hitbox)
        if self._dragged_object != None:
            screen.blit(self._dragged_sprite, (self._dragged_x, self._dragged_y))