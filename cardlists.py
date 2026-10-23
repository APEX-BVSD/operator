import copy

import pygame

from cards import *
from settings import MARGIN_X, MARGIN_Y, SCREEN_HEIGHT


class CardList:
    def __init__(self):
        self.scroll_index: int = 0
        self._card_list: list[Card] = []
        self._dragged_object = None
        self._dragged_sprite = None
        self._dragged_index = None
        self._x_offset: int = 0
        self._y_offset: int = 0
        self.position: tuple[int, int] = (self._x_offset, self._y_offset)
        self._dragged: bool = False

    def scroll_up(self):
        self.scroll_index -= 1
        self._y_offset += CWIDTH

    def scroll_down(self):
        self.scroll_index += 1
        self._y_offset -= CWIDTH

    def process_click(self, x, y):
        """
        Processes a click by checking if it is within an interactable object

        X: the x coordinate of the click
        Y: the y coordinate of the click
        """

        counter: int = 0

        for object in self._card_list:
            if (
                x >= object.hitbox.left + object.position[0]
                and x <= object.hitbox.right + object.position[0]
                and y >= object.hitbox.top + object.position[1]
                and y <= object.hitbox.bottom + object.position[1]
            ):
                self._dragged_object = object
                self._dragged_sprite = pygame.Surface.copy(object.image)
                self._dragged_index = counter
                pygame.Surface.set_alpha(self._dragged_sprite, 100)
            counter += 1

    def check_card_movement(self, x, y, cards, index):
        """
        Checks if cards need to be moved after a drag stops

        X: the x coordinate of the cursor
        Y: the y coordinate of the cursor
        """
        if len(self._card_list) != 0:
            if (
                x >= self._x_offset - 50
                and x <= (len(self._card_list) + 1) * 100 - 50 + self._x_offset
                and y
                <= self._card_list[0].hitbox.bottom + self._card_list[0].position[1]
                and y >= self._card_list[0].hitbox.top + self._card_list[0].position[1]
            ):
                new_index: int = (x - 50 - self._x_offset) // 100 + 1
                if cards == self:
                    if new_index > index:
                        self._card_list.insert(new_index, self._card_list[index])
                        cards._card_list.pop(index)

                    elif index == new_index:
                        pass

                    else:
                        self._card_list.insert(new_index, self._card_list[index])
                        cards._card_list.pop(index + 1)
                else:
                    self._card_list.insert(new_index, cards._card_list[index])
                    cards._card_list.pop(index)

        else:
            if (
                x >= self._x_offset - 50
                and x <= 50 + self._x_offset
                and y <= self._y_offset + 100
                and y >= self._y_offset
            ):
                self._card_list.append(cards._card_list[index])
                cards._card_list.pop(index)

        self._dragged = False

    def set_card_position(self):
        counter: int = copy.copy(self.scroll_index)
        for card in self._card_list:
            card.position = (CWIDTH * counter + self._x_offset, self._y_offset)
            counter += 1

    def cards(self):
        return self._card_list

    def clear_cards(self):
        self._card_list.clear()


class HorizontalList(CardList):
    def __init__(self):
        self.scroll_index = 0
        CardList.__init__(self)
        self._card_list: list[Card]
        self._x_offset: int = CWIDTH + MARGIN_X
        self._y_offset: int = SCREEN_HEIGHT - CWIDTH - MARGIN_X // 3
        self.position: tuple[int, int] = (self._x_offset, self._y_offset)
        self._dragged: bool = False
        self._bounding_box: pygame.Rect = pygame.Rect(
            self._x_offset, self._y_offset, CWIDTH * 5, CWIDTH
        )
        self.image: pygame.Surface = pygame.transform.scale(
            pygame.image.load("assets/listbg.png"),
            (self._bounding_box.width, self._bounding_box.height),
        )


class VerticalList(CardList):
    def __init__(self):
        CardList.__init__(self)
        self._x_offset = MARGIN_X // 3
        self._y_offset = MARGIN_Y + CWIDTH // 4
        self.position = (self._x_offset, self._y_offset)
        self._card_list: list[Card] = [random_card(0), random_card(0)]
        self._bounding_box: pygame.Rect = pygame.Rect(
            self._x_offset, self._y_offset, CWIDTH, CWIDTH * 5
        )
        self.image: pygame.Surface = pygame.Surface(
            (self._bounding_box.width, self._bounding_box.height), pygame.SRCALPHA
        )
        self.image.blit(
            pygame.transform.scale(
                pygame.transform.rotate(pygame.image.load("assets/listbg.png"), 90),
                (self._bounding_box.width, self._bounding_box.height),
            )
        )

    def append(self, c: Card):
        self._card_list.append(c)

    def process_click(self, x, y):
        """
        Processes a click by checking if it is within an interactable object

        X: the x coordinate of the click
        Y: the y coordinate of the click
        """

        counter: int = 0

        for object in self._card_list:
            if (
                x >= object.hitbox.left + object.position[0]
                and x <= object.hitbox.right + object.position[0]
                and y >= object.hitbox.top + object.position[1]
                and y <= object.hitbox.bottom + object.position[1]
            ):
                self._dragged_object = object
                self._dragged_sprite = pygame.Surface.copy(object.image)
                self._dragged_index = counter
                self._dragged = True
                pygame.Surface.set_alpha(self._dragged_sprite, 100)
            counter += 1

    def check_card_movement(self, x, y, list, index):
        """
        Checks if cards need to be moved after a drag stops

        X: the x coordinate of the cursor
        Y: the y coordinate of the cursor
        """
        if len(self._card_list) != 0:
            if (
                y > self._y_offset - 50
                and y <= (len(self._card_list) + 1) * 100 - 50 + self._y_offset
                and x
                <= self._card_list[0].hitbox.right + self._card_list[0].position[0]
                and x >= self._card_list[0].hitbox.left + self._card_list[0].position[0]
            ):
                new_index: int = (y - 50 - self._y_offset) // 100 + 1
                if list == self:
                    if new_index > index:
                        self._card_list.insert(new_index, self._card_list[index])
                        list._card_list.pop(index)

                    elif index == new_index:
                        pass

                    else:
                        self._card_list.insert(new_index, self._card_list[index])
                        list._card_list.pop(index + 1)
                else:
                    self._card_list.insert(new_index, list._card_list[index])
                    list._card_list.pop(index)

        else:
            if (
                y >= self._y_offset - 50
                and y <= 50 + self._y_offset
                and x <= self._x_offset + 100
                and x >= self._x_offset
            ):
                self._card_list.append(list._card_list[index])
                list._card_list.pop(index)

        self._dragged = False

    def set_card_position(self):
        counter: int = 0
        for card in self._card_list:
            card.position = (self._x_offset, self._y_offset + 100 * counter)
            counter += 1
