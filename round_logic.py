import random
from cards import *
import pygame

random_card_amount: int = 2
CARD_IDS: dict = {1: Card, 2: Card}
cards: list = []
base_number: int = -1

def initialize_round():
    '''
    Assigns starting values and cards to the round
    '''
    cards.clear()
    for _ in range(random_card_amount):
        cards.append(CARD_IDS[random.randint(1,len(CARD_IDS))])
    return random.randint(1,100) # Maybe have this change as the game goes on?

def run_round(number):
    '''
    Handles round logic after intilizing and before ending
    '''
    for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    run_round_math(number)
                    return False
    return True
def run_round_math(number):
    '''
    Handles the math at round end 
    '''
    
    final_number: int = number

    for card in cards:
        final_number = card.run_card(final_number)
    print(final_number)