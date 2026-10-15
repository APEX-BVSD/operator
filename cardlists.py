import pygame
from cards import *

class CardList():

    _card_list: list[Card] = []
    _scroll_offset: int = 0
    _dragged_obj = None
    _dragged_sprite = None
    _dragged_index = None
    _x_offset: int = 0
    _y_offset: int = 0
    _is_vertical: bool = False

    def __init__(self, cards: list[Card], x: int, y: int, vertical: bool):
        self._card_list = cards
        self._is_vertical = vertical
        self._x_offset = x
        self._y_offset = y

    def process_click(self, x, y):
        '''
        Processes a click by checking if it is within an interactable object

        X: the x coordinate of the click
        Y: the y coordinate of the click
        '''

        counter: int = 0 

        for obj in self._card_list:
            if x >= obj.hitbox.left + obj.position[0] and x <= obj.hitbox.right + obj.position[0] and y >= obj.hitbox.top + obj.position[1] and y <= obj.hitbox.bottom + obj.position[1]:
                self._dragged_obj = obj
                self._dragged_sprite = pygame.Surface.copy(obj.image)
                self._dragged_index = counter
                pygame.Surface.set_alpha(self._dragged_sprite, 100)
            counter += 1

    def check_card_movement(self, x, y, ls, index):
        '''
        Checks if cards need to be moved after a drag stops

        X: the x coordinate of the cursor
        Y: the y coordinate of the cursor    
        '''

        
        
        if x >= self._x_offset and x <= (len(self._card_list) + 1) * 100 - 50 + self._x_offset and y <= self._card_list[0].hitbox.bottom + self._card_list[0].position[1] and y >= self._card_list[0].hitbox.top + self._card_list[0].position[1]:
            new_index: int = (x - 50 - self._x_offset) // 100 + 1
            if ls == self:
                if new_index > index:
                    self._card_list.insert(new_index, self._card_list[index])
                    ls._card_list.pop(index)

                elif index == new_index:
                    pass

                else:
                    self._card_list.insert(new_index, self._card_list[index])
                    ls._card_list.pop(index + 1)
            else:
                self._card_list.insert(new_index, ls._card_list[index])
                ls._card_list.pop(index)

        elif y > self._y_offset and y <= (len(self._card_list) + 1) * 100 - 50 + self._y_offset and x <= self._card_list[0].hitbox.right + self._card_list[0].position[0] and x >= self._card_list[0].hitbox.left + self._card_list[0].position[0] and self._is_vertical:
            new_index: int = (y - 50 - self._y_offset) // 100 + 1
            if ls == self:
                if new_index > index:
                    self._card_list.insert(new_index, self._card_list[index])
                    ls._card_list.pop(index)

                elif index == new_index:
                    pass

                else:
                    self._card_list.insert(new_index, self._card_list[index])
                    ls._card_list.pop(index + 1)
            else:
                self._card_list.insert(new_index, ls._card_list[index])
                ls._card_list.pop(index)

        self._dragged = False
        

    def set_card_position(self):
        counter: int = 0
        for card in self._card_list:
            if not self._is_vertical:
                card.position = (100 * counter + self._x_offset, self._y_offset)
            else:
                card.position = (self._x_offset, self._y_offset + 100 * counter)
            counter += 1

    def populate(self, n: int):
        for _ in range(n):
            self._card_list.append(random_card(5)) # arbitrary constant for testing purposes REMOVE ME
