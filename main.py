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
from game_screen import *

async def main() -> None:

    round_initialized: bool = False

    pygame.init()

    # set the screen dimensions
    screen: pygame.Surface = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

    # create the UI
    ui: UI = UI()

    # set title
    pygame.display.set_caption(GAME_TITLE)

    # create clock
    clock: pygame.time.Clock = pygame.time.Clock()


    # MAIN GAME LOOP
    running: bool = True
    game_state: str = "START_SCREEN"
    game_screen: GameScreen = GameScreen()
    while running:

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if game_state == "START_SCREEN":
            game_state = display_start_screen(screen)

        elif game_state == "PLAYING":
            if not round_initialized: 
                base_number: int = initialize_round()
                round_initialized = True 
            game_screen.display_game_screen(screen) 
            
        elif game_state == "GAME_OVER":
            pass

        else:
            print(f"Invalid game state: {game_state}")
            running = False

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                run_round_math(base_number)
                round_initialized = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click_x, click_y = event.pos
                ui.process_click(click_x,click_y)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                ui.check_card_movement(mouse_x, mouse_y)
                ui._dragged_object = None
                ui._dragged_sprite = None
                ui._dragged_index = None

        ui.move_dragged(mouse_x, mouse_y)
        ui.draw_objects(screen)
        
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