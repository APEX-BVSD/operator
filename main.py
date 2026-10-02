"""
Describe your game.
Month Year
First Last
First Last 
First Last 
"""

import asyncio
from enum import Enum
import pygame

from settings import *
from start_screen import *
from cards import *
from player import *

test_player: Player = Player()
a: AddingCard = AddingCard()
m: MultiplyCard = MultiplyCard()
test_player.add_card(AddingCard)
test_player.add_card(MultiplyCard)

async def main() -> None:

    pygame.init()

    # set the screen dimensions
    screen: pygame.Surface = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

    # set title
    pygame.display.set_caption(GAME_TITLE)

    # create clock
    clock: pygame.time.Clock = pygame.time.Clock()


    # MAIN GAME LOOP
    running: bool = True
    game_state: str = "START_SCREEN"
    while running:
        if game_state == "START_SCREEN":
            test_player.calculate_score(14)
            print(test_player.get_score())

        elif game_state == "PLAYING":
            pass

        elif game_state == "GAME_OVER":
            pass

        else:
            print(f"Invalid game state: {game_state}")
            running = False


        
        # render the screen
        pygame.display.flip()
        # advance the clock
        clock.tick(FPS)
        pygame.event.pump()

        await asyncio.sleep(0)

    # when the loop breaks, shut down pygame gracefully
    pygame.quit()


asyncio.run(main())