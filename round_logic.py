import random
from cards import *
import pygame
from game_screen import *
from uicontrol import *

random_card_amount: int = 2
CARD_IDS: dict = {1: Card(), 2: Card()}
cards: list = []
base_number: int = -1

def initialize_round():
    '''
    Assigns starting values and cards to the round

    Returns the base number
    '''
    cards.clear()
    for _ in range(random_card_amount):
        cards.append(CARD_IDS[random.randint(1,len(CARD_IDS))])
    number:int = random.randint(1,100) # Maybe have this change as the game goes on?
    GameScreen.current_number = number
    return number

def run_round_math(number):
    '''
    Handles the math at round end 

    number: number math is being done on
    '''
    
    final_number: int = number

    for card in cards:
        final_number = card.apply(final_number)
    print(final_number)