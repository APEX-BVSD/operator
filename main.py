"""
Describe your game.
Sep 2026
Elizabeth Posusta
Carter Quarles
First Last
"""

import asyncio

import pygame

from buttons import *
from cards import Card
from game_screen import *
from round_logic import *
from settings import *
from start_screen import *

def test() -> None:
    print("this is a test!")

async def main() -> None:

    round_initialized: bool = False
    reset_values: bool = False

    pygame.init()

    # set the screen dimensions
    screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

    test_button: Button = Button(
        test,
        "assets/cardbg.png",
        "PAUSE",
        (100, 100),
        (0, 0),
        "assets/fonts/sambaisdead.ttf",
    )

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
                base_number: int = initialize_round()
                round_initialized = True
            game_screen.display_game_screen(screen)
            ui.move_dragged(mouse_x, mouse_y)
            ui.draw_objects(screen)
            screen.blit(test_button.image)

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
                ui.process_list_click(click_x, click_y)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if ui._dragged_object != None:
                    ui.check_list_card_movement(mouse_x, mouse_y)
                reset_values = True

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
