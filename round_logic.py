import random
from cards import *
import pygame
from game_screen import *
from uicontrol import *

random_card_amount: int = 2
base_number: int = -1

def initialize_round(cards: list[Card]):
    '''
    Assigns starting values and cards to the round
    '''
    vertical_list.clear_cards()
    for card in cards:
        vertical_list._card_list.append(card)

    horizontal_list._card_list.clear()
    # for card in cards:
        # horizontal_list._card_list.append(card)

    # horizontal_list._card_list.clear()

    for _ in range(random_card_amount):
         horizontal_list._card_list.append(random_card(5))


    number:int = random.randint(1,100) # Maybe have this change as the game goes on?
    GameScreen.current_number = number
    return number

def run_round_math(number):
    '''
    Handles the math at round end
    '''

    final_number: int = number

    for card in horizontal_list._card_list:
        final_number = card.apply(final_number)
    print(final_number)
