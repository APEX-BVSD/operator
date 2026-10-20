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

from settings import SCREEN_HEIGHT, SCREEN_WIDTH


class GameScreen:
    current_number: int = -1

    def display_game_screen(self, screen: pygame.Surface):
        """
        Displays the game screen.

        Parameters:
        screen(pygame.Surface): The screen to render the game on

        """

        # draw the screen
        screen.blit(
            pygame.transform.scale(
                pygame.image.load("assets/background.png"),
                (SCREEN_WIDTH, SCREEN_HEIGHT),
            )
        )

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
