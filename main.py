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
from shop import *
from player import *

async def main() -> None:

    round_initialized: bool = False
    reset_values: bool = False

    pygame.init()

    # set the screen dimensions
    screen: pygame.Surface = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

    # create the UI
    ui: UI = UI()

    # create the shop
    shop: Shop = Shop()

    # create the plater
    player: Player = Player()

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

        if reset_values:
            ui.setter(True)
            reset_values = False
        else:
            ui.setter(False)

        if game_state == "START_SCREEN":
            game_state = display_start_screen(screen)

        elif game_state == "PLAYING":
            if not round_initialized: 
                base_number: int = initialize_round(player._cards)
                round_initialized = True 
            game_screen.display_game_screen(screen) 
            ui.move_dragged(mouse_x, mouse_y)
            ui.draw_objects(screen)

        elif game_state == "SHOP":
            shop.draw_objects(screen)
        
        elif game_state == "GAME_OVER":
            pass

        else:
            print(f"Invalid game state: {game_state}")
            running = False

        for event in pygame.event.get():
            if game_state == "PLAYING":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    run_round_math(base_number)
                    round_initialized = False
                    game_state = "SHOP"
                    shop.initialize_shop()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click_x, click_y = event.pos
                    ui.process_list_click(click_x,click_y)
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    ui.check_list_card_movement(mouse_x, mouse_y)
                    reset_values = True
            elif game_state == "SHOP":
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click_x, click_y = event.pos
                    shop_output = shop.process_click(click_x, click_y)
                    if isinstance(shop_output, str):
                        game_state = shop_output
                    else:
                        player._cards.append(shop_output) 
        
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