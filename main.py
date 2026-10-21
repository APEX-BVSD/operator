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
from player import *
from round_logic import *
from settings import *
from start_screen import *
from uicontrol import *
from shop import *

player: Player = Player()
shop: Shop = Shop()
buttons: list[Button] = []

def submit(p: Player) -> None:
    p.game_state = "SCORE"

async def main() -> None:

    round_initialized: bool = False
    reset_values: bool = False

    pygame.init()

    # set the screen dimensions
    screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create the UI
    ui: UI = UI()

    # create the shop
    # shop: Shop = Shop()

    # create the plater
    player: Player = Player()

    # set title
    pygame.display.set_caption(GAME_TITLE)

    # create clock
    clock: pygame.time.Clock = pygame.time.Clock()

    # MAIN GAME LOOP
    running: bool = True
    game_screen: GameScreen = GameScreen()

    submit_button: Button = Button(
        submit,
        "assets/submit.png",  # "assets/submit.png"
        "",
        (100, 100),
        (SCREEN_WIDTH - MARGIN_X - CWIDTH, MARGIN_Y),
        "assets/fonts/sambaisdead.ttf",
    )
    buttons.append(submit_button)

    round_num: int = 0

    while running:
        base_number: int

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if reset_values:
            ui.setter(True)
            reset_values = False
        else:
            ui.setter(False)

        if player.game_state == "START_SCREEN":
            player.game_state = display_start_screen(screen)

        elif game_state == "PLAYING":
            round_num += 1
            if not round_initialized:
                base_number: int = initialize_round(player.get_cards(), round_num)
                round_initialized = True
            game_screen.display_game_screen(screen)
            ui.move_dragged(mouse_x, mouse_y)
            ui.draw_objects(screen)
            screen.blit(submit_button.image, submit_button.pos)

        elif game_state == "SCORE":
            player.set_cards(horizontal_list.cards())
        #     for c in ui.get_lists()[0].cards():
        #         player.add_scoring_card(c)
            player.calculate_score(base_number)
            # player.bonus_score()

            print(player.get_score())


            shop.initialize_shop()
            player.game_state = "SHOP"

        elif player.game_state == "SHOP":
            shop.draw_objects(screen)

        elif player.game_state == "GAME_OVER":
            pass

        else:
            print(f"Invalid game state: {player.game_state}")
            running = False

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click_x, click_y = event.pos
                for b in buttons:
                    if b.click_bb.collidepoint(event.pos):
                        b.function(player)
                if player.game_state == "PLAYING":
                    ui.process_list_click(click_x, click_y)

                if player.game_state == "SHOP":
                    shop_output = shop.process_click(click_x, click_y, player)

                    if shop_output == "PLAYING":
                        player.game_state = "PLAYING"
                        round_initialized = False

                    elif isinstance(shop_output, Card):
                        player.add_card(shop_output)
                    
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
