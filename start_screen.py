"""
Contains functions that implement the start screen.
Month Year
First Last
First Last 
First Last 
"""


import pygame
import math
from pygame import font
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

# Keep track of animation timing across frames
animation_timer: float = 0.0

def display_start_screen(screen: pygame.Surface) -> str:

    global animation_timer
    
    # 1. Creative Dynamic Background (A smooth, subtle breathing pulse effect)
    # Oscillates between 15 and 45 to create an ambient midnight-blue glow
    pulse_intensity = int(30 + 15 * math.sin(animation_timer))
    screen.fill((20, 24, pulse_intensity))
    animation_timer += 0.05 # Controls how fast the background pulses

    # 2. Setup Fonts safely
    title_font = pygame.font.Font(None, 74)
    prompt_font = pygame.font.Font(None, 36)

    # 3. Render Title Text with a Drop-Shadow Effect
    title_string = "[Title]"
    title_shadow = title_font.render(title_string, True, (10, 12, 20))
    title_main = title_font.render(title_string, True, (255, 215, 0)) # Gold text
    
    title_x = SCREEN_WIDTH // 2 - title_main.get_width() // 2
    title_y = SCREEN_HEIGHT // 3
    
    # Blit shadow slightly offset down and right, then blit the main title over it
    screen.blit(title_shadow, (title_x + 3, title_y + 3))
    screen.blit(title_main, (title_x, title_y))

    # 4. Render Action Prompt with a Fading Visual Effect
    # Makes the text smoothly fade in and out to grab player attention
    alpha_fade = int(155 + 100 * math.sin(animation_timer * 2))
    prompt_text = prompt_font.render("Press SPACE to start.", True, (200, 200, 255))
    
    # Set the transparency (alpha) level on the text surface container
    prompt_text.set_alpha(alpha_fade)
    
    prompt_x = SCREEN_WIDTH // 2 - prompt_text.get_width() // 2
    prompt_y = SCREEN_HEIGHT * 2 // 3
    screen.blit(prompt_text, (prompt_x, prompt_y))

    # 5. Process Input Event Loops Without Blocking Window Controls
    for event in pygame.event.get():
        # Cleanly exits the window if the user hits the top corner close button
        if event.type == pygame.QUIT:
            return "QUIT"
            
        # Safe game transition triggers
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            return "PLAYING"

    # Maintain screen loop sequence
    return "START_SCREEN"


