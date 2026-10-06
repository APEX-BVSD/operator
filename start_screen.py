"""
Contains functions that implement the start screen.
Month 2026
First Last
First Last 
First Last 
"""


import pygame
from pygame import font

def display_start_screen(screen: pygame.Surface) -> str:
    """
    Displays the start screen text and waits for the player to press the space key.
    Returns "PLAYING" as the next game state.
    """
    # Clear the screen with a clean background color
    screen.fill((20, 24, 35))

    # Initialize font styles safely using Pygame defaults
    title_font = pygame.font.Font(None, 80)
    prompt_font = pygame.font.Font(None, 40)

    # Render and center the Placeholder Title
    title_text = title_font.render("[Title]", True, (255, 255, 0))
    title_x = screen.get_width() // 2 - title_text.get_width() // 2
    title_y = screen.get_height() // 3
    screen.blit(title_text, (title_x, title_y))

    # Render and center the action prompt
    prompt_text = prompt_font.render("Press SPACE to start.", True, (200, 200, 255))
    prompt_x = screen.get_width() // 2 - prompt_text.get_width() // 2
    prompt_y = screen.get_height() * 2 // 3
    screen.blit(prompt_text, (prompt_x, prompt_y))

    # Process the events, if the space button was pressed, move to the next screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "QUIT"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            return "PLAYING"

    # Stay on the current screen
    return "START_SCREEN"


