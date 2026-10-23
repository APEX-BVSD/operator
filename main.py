"""
SMOOTH OPERATOR is an incremental game where you use mathematical OPERATIONS to maximize your SCORE
Sep 2026
Elizabeth Posusta
Carter Quarles
"""

# TODO: cap number of cards in horizontal_list at 5
#       add scrollbar to vertical_list
#       tutorial screen

import asyncio

import pygame

from buttons import *
from cardlists import *
from cards import Card
from game_screen import *
from player import *
from round_logic import *
from settings import *
from shop import *
from start_screen import *
from uicontrol import *

player: Player = Player()

shop: Shop = Shop()
buttons: list[Button] = []


# set the screen dimensions
screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# create the UI
ui: UI = UI()


def submit(p: Player) -> None:
    p.game_state = "SCORE"


def pause(p: Player) -> None:
    p.game_state = "PAUSE"


def down(p: Player, cl: CardList):
    if len(cl.cards()) <= 5 and len(p.get_cards()) <= 5:
        return
    cl.scroll_down()


def up(p: Player, cl: CardList):
    if len(cl.cards()) <= 5 or cl.scroll_index == 0:
        return
    cl.scroll_up()


async def main() -> None:

    round_initialized: bool = False
    reset_values: bool = False
    button_pressed: bool = False

    pygame.init()
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

    howtoplay: pygame.Surface = pygame.transform.scale(
        pygame.image.load("assets/howtoplay.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    submit_button: Button = Button(
        submit,
        "assets/submit.png",
        "",
        (CWIDTH, CWIDTH),
        (SCREEN_WIDTH - MARGIN_Y - CWIDTH, MARGIN_Y),
        "assets/fonts/sambaisdead.ttf",
    )

    pause_button: Button = Button(
        pause,
        "assets/pause.png",
        "",
        (CWIDTH, CWIDTH),
        (SCREEN_WIDTH - MARGIN_X * 2, SCREEN_HEIGHT - 5 * (MARGIN_Y // 2)),
        "assets/fonts/sambaisdead.ttf",
    )

    scroll_down: Button = Button(
        down,
        "assets/scrolldown.png",
        "",
        (CWIDTH // 2, CWIDTH // 2),
        (CWIDTH // 2, SCREEN_HEIGHT - (2 * (CWIDTH // 3))),
        "assets/fonts/sambaisdead.ttf",
    )

    scroll_up: Button = Button(
        up,
        "assets/scrollup.png",
        "",
        (CWIDTH // 2, CWIDTH // 2),
        (CWIDTH // 2, 2 * (CWIDTH // 3)),
        "assets/fonts/sambaisdead.ttf",
    )

    buttons.append(submit_button)
    buttons.append(pause_button)
    buttons.append(scroll_down)
    buttons.append(scroll_up)

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

        elif player.game_state == "PAUSE":
            screen.blit(howtoplay)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                    player.game_state = "PLAYING"

        elif player.game_state == "PLAYING":
            if not round_initialized:
                base_number: int = initialize_round(player.get_cards(), round_num)
                round_initialized = True
            game_screen.display_game_screen(screen, player)
            ui.move_dragged(mouse_x, mouse_y)
            ui.draw_objects(screen)

            for b in buttons:
                screen.blit(b.image, b.pos)

        elif player.game_state == "SCORE":
            #    player.set_cards(horizontal_list.cards())
            #     for c in ui.get_lists()[0].cards():
            #         player.add_scoring_card(c)
            player.calculate_score(base_number, horizontal_list._card_list)
            # player.bonus_score()

            print(player.get_score())

            shop.initialize_shop()
            round_num += 1
            player.game_state = "SHOP"

        elif player.game_state == "SHOP":
            shop.draw_objects(screen)

        elif player.game_state == "GAME_OVER":
            pass

        else:
            print(f"Invalid game state: {player.game_state}")
            running = False

        for event in pygame.event.get():
            button_pressed = False
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click_x, click_y = event.pos
                for b in buttons:
                    if b.click_bb.collidepoint(event.pos):
                        button_pressed = True
                        if b == scroll_down or b == scroll_up:
                            b.function(player, vertical_list)
                        else:
                            b.function(player)
                if not button_pressed:
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
