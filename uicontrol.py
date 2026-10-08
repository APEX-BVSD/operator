import pygame
from settings import *
from objects import *
import pygame
from settings import *


class UI():
    _clickable_objects: list = []
    _vertical_list: list = []
    _horizontal_list: list = [Placeholder1, Placeholder2, Placeholder3]
    _drawn_objects: list = [Placeholder1, Placeholder2, Placeholder3]
    _dragged_object = None
    _dragged_sprite = None
    _dragged_index = None
    _dragged_x: int = 0
    _dragged_y: int = 0
    

    def process_click(self, x, y):
        '''
        Processes a click by checking if it is within an interactable object

        X: the x coordinate of the click
        Y: the y coordinate of the click
        '''

        counter: int = 0 

        for object in self._horizontal_list:
            if x >= object.hitbox.left + object.position[0] and x <= object.hitbox.right + object.position[0] and y >= object.hitbox.top + object.position[1] and y <= object.hitbox.bottom + object.position[1]:
                self._dragged_object = object
                self._dragged_sprite = pygame.Surface.copy(object.image)
                self._dragged_index = counter
                pygame.Surface.set_alpha(self._dragged_sprite, 100)
                

    def move_dragged(self, x, y):
        '''
        Updates the position of the dragged object if there is one

        X: the x coordinate of the cursor
        Y: the y coordinate of the cursor    
        '''

        counter: int = 0
        
        if self._dragged_object != None:
            self._dragged_x = x - (self._dragged_object.hitbox.width / 2)
            self._dragged_y = y - (self._dragged_object.hitbox.height / 2)

        for card in self._horizontal_list:
            card.position = (100 * counter, 0)
            counter += 1

    def check_card_movement(self, x, y):
        '''
        Checks if cards need to be moved after a drag stops

        X: the x coordinate of the cursor
        Y: the y coordinate of the cursor    
        '''
        if x <= (len(self._horizontal_list) + 1) * 100 - 50 and y <= 100:
            new_index: int = (x - 50) // 100 + 1
            if new_index > self._dragged_index:
                self._horizontal_list.insert(new_index, self._horizontal_list[self._dragged_index])
                self._horizontal_list.pop(self._dragged_index)

            elif self._dragged_index == new_index:
                pass

            else:
                self._horizontal_list.insert(new_index, self._horizontal_list[self._dragged_index])
                self._horizontal_list.pop(self._dragged_index - 1)
            print(new_index)
            print(self._horizontal_list)

    def draw_objects(self, screen: pygame.Surface):  
        '''
        Draws UI elements onto the screen

        screen: the game screen to be drawn on        
        '''
        
        for object in self._drawn_objects:
            screen.blit(object.image, object.position)
          
        if self._dragged_object != None:
            screen.blit(self._dragged_sprite, (self._dragged_x, self._dragged_y))