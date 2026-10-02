import random
from cards import *
import pygame
from game_screen import *
from uicontrol import *

random_card_amount: int = 2
CARD_IDS: dict = {1 : AddingCard, 2: MultiplyCard}
cards: list = []
base_number: int = -1

def initialize_round():
    '''
    Assigns starting values and cards to the round
    '''
    cards.clear()
    for _ in range(random_card_amount):
        cards.append(CARD_IDS[random.randint(1,len(CARD_IDS))])
    number:int = random.randint(1,100) # Maybe have this change as the game goes on?
    GameScreen.current_number = number
    return number
    
def run_round(number) -> bool:
    '''
    Handles round logic after intilizing and before ending

    Returns true or flase depending on if the round should be reset
    '''
    for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    run_round_math(number)
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = event.pos
                    

    return True

def run_round_math(number):
    '''
    Handles the math at round end 
    '''
    
    final_number: int = number

    for card in cards:
        final_number = card.run_card(final_number)
    GameScreen.current_number = final_number
    print(final_number)