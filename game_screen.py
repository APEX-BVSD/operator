"""
Contains functions that implement the game play. Break this into further files as
it gets more complex.
Month Year
First Last
First Last
First Last
"""

import pygame
from pygame import font
from pygame.constants import SRCALPHA
from pygame.surface import Surface

from buttons import TextBox
from player import Player
from settings import MARGIN_X, MARGIN_Y, SCREEN_HEIGHT, SCREEN_WIDTH


def display_score(p: Player):
    score_display: TextBox = TextBox(
        Surface((SCREEN_WIDTH, SCREEN_HEIGHT), SRCALPHA),
        str(int(p.get_score())),
        (2 * SCREEN_WIDTH // 3, SCREEN_HEIGHT // 10),
        (0, 0),
        "assets/fonts/homevideo.ttf",
        True,
    )
    return score_display.image


class GameScreen:
    current_number: int = -1

    bg_img = pygame.image.load("assets/background.png")
    bg_frame = pygame.transform.scale(
                pygame.image.load("assets/bg_frame.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)
            )

    def display_game_screen(self, screen: pygame.Surface, player: Player):
        """
        Displays the game screen.

        Parameters:
        screen(pygame.Surface): The screen to render the game on

        """

        bg = pygame.transform.scale(self.bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

        bg.blit(self.bg_frame)

        bg.blit(display_score(player))

        # draw the screen
        screen.blit(bg)

        base_font: pygame.font.Font = pygame.font.Font(
            "assets/fonts/02.10ITA.TTF", size=128
        )
        text_box: pygame.Surface = base_font.render(
            str(self.current_number), True, "white"
        )
        screen.blit(
            text_box,
            (
                screen.get_width() // 2 - text_box.get_width() // 2,
                screen.get_height() // 2 - text_box.get_height() // 2,
            ),
        )
