import pygame
from settings import *
from cards import *

class Shop():

    _available_cards: list = []
    _cards_per_row: int = 3
    _exit_button: pygame.Rect = pygame.Rect(300,
                                            400,
                                            200, 100
    )

    def process_click(self, x: int, y: int, player):
        '''
        Processes a click by checking if you clicked on a card, then removes the purchased card

        X: the x coordinate of the click
        Y: the y coordinate of the click

        Returns: Either gamestate if the exit button is clicked, or a card if you purchase one
        '''

        counter: int = 0 

        for obj in self._available_cards:
            if x >= obj.hitbox.left + obj.position[0] and x <= obj.hitbox.right + obj.position[0] and y >= obj.hitbox.top + obj.position[1] and y <= obj.hitbox.bottom + obj.position[1]:
                if player.get_score() >= obj.cost:
                    player.set_score(player.get_score() - obj.cost)
                    print(player.get_score())
                    bought_card = self._available_cards[counter]
                    self._available_cards.pop(counter)
                    return bought_card
                else:
                    return
            counter += 1

        if x >= self._exit_button.left and x <= self._exit_button.right and y >= self._exit_button.top and y <= self._exit_button.bottom:
            return "PLAYING"

    def initialize_shop(self):
        '''
        Sets initial values for the shop and generates cards to be purchased
        '''
        self._available_cards.clear()

        for _ in range(6):
            self._available_cards.append(random_card(5))

        counter: int = 0
        
        for card in self._available_cards:
            card.position = ((SCREEN_WIDTH -(self._cards_per_row * 100)) // 2 + (counter % 3) * 100, 100 + counter // self._cards_per_row * 100)
            counter += 1

    def draw_objects(self, screen: pygame.Surface):  
        '''
        Draws UI elements onto the screen

        screen: the game screen to be drawn on        
        '''

        screen.fill("green")
        
        pygame.draw.rect(screen, (100, 100, 100), self._exit_button)
        
        for card in self._available_cards:
            screen.blit(card.image, card.position)