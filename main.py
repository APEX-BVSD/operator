"""
Describe your game.
Month Year
First Last
First Last 
First Last 
"""

import asyncio
import pygame
from settings import *
from start_screen import *
from cards import *
from round_logic import *


async def main() -> None:

    round_initialized: bool = False

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
            game_state = display_start_screen(screen)

        elif game_state == "PLAYING":
            if not round_initialized: 
                base_number: int = initialize_round()
                round_initialized = True
            round_initialized = run_round(base_number)
            
            
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
    print("Running loop ended.")
    pygame.quit()


asyncio.run(main())