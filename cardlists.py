import pygame
from objects import *

class CardList():

    _card_list: list = []
    _scroll_offset: int = 0
    _dragged_object = None
    _dragged_sprite = None
    _dragged_index = None

    def process_click(self, x, y):
        print("You're doing something wrong")

class HorizontalList(CardList):

    _card_list: list = [Placeholder1, Placeholder2, Placeholder3, Placeholder4, Placeholder5, Placeholder6]

    def process_click(self, x, y):
        '''
        Processes a click by checking if it is within an interactable object

        X: the x coordinate of the click
        Y: the y coordinate of the click
        '''

        counter: int = 0 

        for object in self._card_list:
            if x >= object.hitbox.left + object.position[0] and x <= object.hitbox.right + object.position[0] and y >= object.hitbox.top + object.position[1] and y <= object.hitbox.bottom + object.position[1]:
                self._dragged_object = object
                self._dragged_sprite = pygame.Surface.copy(object.image)
                self._dragged_index = counter
                pygame.Surface.set_alpha(self._dragged_sprite, 100)
            counter += 1

    def check_card_movement(self, x, y):
        '''
        Checks if cards need to be moved after a drag stops

        X: the x coordinate of the cursor
        Y: the y coordinate of the cursor    
        '''
        if x <= (len(self._card_list) + 1) * 100 - 50 and y <= self._card_list[0].hitbox.bottom + self._card_list[0].position[1] and y >= self._card_list[0].hitbox.top + self._card_list[0].position[1]:
            new_index: int = (x - 50) // 100 + 1
            if new_index > self._dragged_index:
                self._card_list.insert(new_index, self._card_list[self._dragged_index])
                self._card_list.pop(self._dragged_index)

            elif self._dragged_index == new_index:
                pass

            else:
                self._card_list.insert(new_index, self._card_list[self._dragged_index])
                self._card_list.pop(self._dragged_index + 1)

    def set_card_position(self):
        counter: int = 0
        for card in self._card_list:
            card.position = (100 * counter, 300)
            counter += 1

class VerticalList(CardList):

    card_list: list = [Placeholder1, Placeholder2, Placeholder3, Placeholder4, Placeholder5, Placeholder6]
    
    def process_click(self, x, y):
        '''
        Processes a click by checking if it is within an interactable object

        X: the x coordinate of the click
        Y: the y coordinate of the click
        '''

        counter: int = 0 

        for object in self._card_list:
            if x >= object.hitbox.left + object.position[0] and x <= object.hitbox.right + object.position[0] and y >= object.hitbox.top + object.position[1] and y <= object.hitbox.bottom + object.position[1]:
                self._dragged_object = object
                self._dragged_sprite = pygame.Surface.copy(object.image)
                self._dragged_index = counter
                pygame.Surface.set_alpha(self._dragged_sprite, 100)
            counter += 1

    def check_card_movement(self, x, y):
        '''
        Checks if cards need to be moved after a drag stops

        X: the x coordinate of the cursor
        Y: the y coordinate of the cursor    
        '''
        if x <= (len(self._card_list) + 1) * 100 - 50 and x <= self._card_list[0].hitbox.left + self._card_list[0].position[0] and x >= self._card_list[0].hitbox.right + self._card_list[0].position[0]:
            new_index: int = (y - 50) // 100 + 1
            if new_index > self._dragged_index:
                self._card_list.insert(new_index, self._card_list[self._dragged_index])
                self._card_list.pop(self._dragged_index)

            elif self._dragged_index == new_index:
                pass

            else:
                self._card_list.insert(new_index, self._card_list[self._dragged_index])
                self._card_list.pop(self._dragged_index + 1)

    def set_card_position(self):
        counter: int = 0
        for card in self._card_list:
            card.position = (0, 100* counter)
            counter += 1