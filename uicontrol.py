import pygame
from settings import *
from objects import *
import pygame
from settings import *
from cardlists import *

vertical_list: CardList = VerticalList()
horizontal_list: CardList = HorizontalList()

class UI():
    _clickable_objects: list = []
    _card_lists: list[CardList] = [horizontal_list, vertical_list]
    _drawn_objects: list = []
    _dragged_object = None
    _dragged_sprite = None
    _dragged_index = None
    _dragged_list = None
    _dragged_x: int = 0
    _dragged_y: int = 0

    def setter(self, reset: bool):
        if reset:
            self._dragged_object = None
            self._dragged_index = None
            self._dragged_sprite = None
            for list in self._card_lists:
                list._dragged_object = None
                list._dragged_sprite = None
                list._dragged_index = None

        for list in self._card_lists:
            if list._dragged_object != None:
                self._dragged_object = list._dragged_object
                self._dragged_sprite = list._dragged_sprite
                self._dragged_index = list._dragged_index
                self._dragged_list = list
            list.set_card_position()

    def process_list_click(self, x, y):
        '''
        Processes a click by passing it to the cardlists

        X: the x coordinate of the click
        Y: the y coordinate of the click
        '''
        for list in self._card_lists:
            list.process_click(x, y)
        
                

    def move_dragged(self, x, y):
        '''
        Updates the position of the dragged object if there is one

        X: the x coordinate of the cursor
        Y: the y coordinate of the cursor    
        '''
        
        if self._dragged_object != None:
            self._dragged_x = x - (self._dragged_object.hitbox.width / 2)
            self._dragged_y = y - (self._dragged_object.hitbox.height / 2)

    def check_list_card_movement(self, x, y):
        '''
        Checks if cards need to be moved after a drag stops

        X: the x coordinate of the cursor
        Y: the y coordinate of the cursor    
        '''

        for list in self._card_lists:
            list.check_card_movement(x, y, self._dragged_list, self._dragged_index)

    def draw_objects(self, screen: pygame.Surface):  
        '''
        Draws UI elements onto the screen

        screen: the game screen to be drawn on        
        '''
        self._drawn_objects.clear()
        
        for list in self._card_lists:
            for card in list._card_list:
                self._drawn_objects.append(card) 

        for object in self._drawn_objects:
            screen.blit(object.image, object.position)
          
        if self._dragged_object != None:
            screen.blit(self._dragged_sprite, (self._dragged_x, self._dragged_y))