"""
Contains functions that implement the start screen.
Month Year
First Last
First Last 
First Last 
"""


import pygame
from pygame.constants import SRCALPHA
from pygame.surface import Surface

from buttons import TextBox
from player import Player
from settings import MARGIN_X, MARGIN_Y, SCREEN_HEIGHT, SCREEN_WIDTH

class StartScreen:
    current_number: int = -1

    bg_img = pygame.image.load("assets/background.png")

    def display_start_screen(self, screen: pygame.Surface):
        """
        Displays the game screen.

        Parameters:
        screen(pygame.Surface): The screen to render the game on

        """

        bg = pygame.transform.scale(self.bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # draw the screen
        screen.blit(bg)

        base_font: pygame.font.Font = pygame.font.Font(
            "assets/fonts/02.10ITA.TTF", size=48
        )
        text_box: pygame.Surface = base_font.render(
            "PRESS SPACE \n   TO START", True, "white"
        )
        screen.blit(
            text_box,
            (
                screen.get_width() // 2 - text_box.get_width() // 2,
                screen.get_height() // 2 - text_box.get_height() // 2,
            ),
        )


        # process the events, if the space button was pressed, move to the next screen
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return "PLAYING"

        # stay on the current screen
        return "START_SCREEN"


