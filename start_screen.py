"""
Contains functions that implement the start screen.
Month 2026 
First Last
First Last 
First Last 
"""

import pygame
import math
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

def display_start_screen(screen: pygame.Surface) -> str:

    # text font
    title_font: pygame.font.Font = pygame.font.Font(None, 74)
    prompt_font: pygame.font.Font = pygame.font.Font(None, 36)

    # create title text and center it
    title_box: pygame.Surface = title_font.render("Operator", True, (255, 215, 0))
    shadow_box: pygame.Surface = title_font.render("Operator", True, (5, 0, 10))
    title_box.set_alpha(90)
    Prompt_box: pygame.Surface = prompt_font.render("PRESS SPACE TO START", True, (255, 215, 0))

    title_x: int = SCREEN_WIDTH // 2 - title_box.get_width() // 2
    title_y: int = SCREEN_HEIGHT // 3
    screen.blit(title_box, (title_x, title_y))
    screen.blit(shadow_box, (title_x + 5, title_y))

    # centers start prompt
    prompt_x: int = SCREEN_WIDTH // 2 - Prompt_box.get_width() // 2
    prompt_y: int = SCREEN_HEIGHT * 2 // 3
    screen.blit(Prompt_box, (prompt_x, prompt_y))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "QUIT"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            return "PLAYING"

    return "START_SCREEN"


