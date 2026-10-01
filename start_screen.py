"""
Contains functions that implement the start screen.
Month Year
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

    Parameters:
    screen(pygame.Surface): The screen to render the game on
    
    Returns:
    str: The game state the game should use in the next frame
    
    """
    
    # draw the screen        
    screen.fill("black")

    font: pygame.font.Font = pygame.font.Font(size=48)
    text_box: pygame.Surface = font.render("Press SPACE to start.", True, "white")
    screen.blit(text_box, (screen.get_width() // 2 - text_box.get_width() // 2, screen.get_height() // 2))


    # process the events, if the space button was pressed, move to the next screen
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return "PLAYING"

    # stay on the current screen
    return "START_SCREEN"


