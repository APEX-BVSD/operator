"""
Contains functions that implement the start screen.
Month Year
First Last
First Last 
First Last 
"""

import pygame
import math
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

animation_timer: float = 0.0

def display_start_screen(screen: pygame.Surface) -> str:
    global animation_timer

    # backgrownd pulse/glow
    pulse_intensity = int(30 + 15 * math.sin(animation_timer))
    screen.fill((20, 24, pulse_intensity))
    animation_timer += 0.05 

    # text font
    title_font = pygame.font.Font(None, 74)
    prompt_font = pygame.font.Font(None, 36)

    # create title text and center it
    title_main = title_font.render("[Title]", True, (255, 215, 0))
    title_x = SCREEN_WIDTH // 2 - title_main.get_width() // 2
    title_y = SCREEN_HEIGHT // 3
    screen.blit(title_main, (title_x, title_y))

    # centers start prompt
    prompt_x = SCREEN_WIDTH // 2 - prompt_text.get_width() // 2
    prompt_y = SCREEN_HEIGHT * 2 // 3
    screen.blit(prompt_text, (prompt_x, prompt_y))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "QUIT"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            return "PLAYING"

    return "START_SCREEN"


