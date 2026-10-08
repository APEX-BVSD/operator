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
        '''
        Processes a click by checking if it is within an interactable object

        X: the x coordinate of the click
        Y: the y coordinate of the click
        '''
        for object in self._draggable_objects:
            if x >= object.hitbox.left and x <= object.hitbox.right and y >= object.hitbox.top and y <= object.hitbox.bottom:
                self._dragged_object = object
                self._dragged_sprite = pygame.Surface.copy(object.image)
                pygame.Surface.set_alpha(self._dragged_sprite, 50)
                

    def move_dragged(self, x, y):
        '''
        Updates the position of the dragged object if there is one

        X: the x coordinate of the cursor
        Y: the y coordinate of the cursor    
        '''
        if self._dragged_object != None:
            self._dragged_x = x - (self._dragged_object.hitbox.width / 2)
            self._dragged_y = y - (self._dragged_object.hitbox.height / 2)

    def draw_objects(self, screen: pygame.Surface):  
        '''
        Draws UI elements onto the screen

        screen: the game screen to be drawn on        
        '''
        for object in self._drawn_objects:
            screen.blit(object.image, object.hitbox)
        if self._dragged_object != None:
            screen.blit(self._dragged_sprite, (self._dragged_x, self._dragged_y))