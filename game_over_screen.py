"""
Contains functions that implement the game over screen.
Month Year
First Last
First Last 
First Last 
"""

import pygame
import math
from pygame import font
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

# Keep track of animation timing across frames for visual effects
glow_timer: float = 0.0

def display_game_over_screen(screen: pygame.Surface) -> str:
    """
    Displays an enhanced game over screen with large neon red glowing text
    and an interactive restart button that routes back to the start screen.

    Parameters:
    screen (pygame.Surface): The main Pygame display surface window.

    Returns:
    str: The target game state tag evaluated for the next frame engine tick.
    """
    global glow_timer
    
    # 1. Dark, moody background to make neon colors stand out
    screen.fill((15, 10, 15))
    glow_timer += 0.06

    # Get current mouse coordinates and click states for button interactions
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_clicked = pygame.mouse.get_pressed()[0] # True if left mouse button is down

    # 2. Setup Fonts safely
    title_font = pygame.font.Font(None, 110) # Large scale font for title
    button_font = pygame.font.Font(None, 36)

    # 3. Create a Large Neon Red "Gameover" Glow Effect
    title_string = "Gameover"
    
    # Calculate an oscillating size for the blur halo to mimic electric flickering
    glow_radius = int(4 + 2 * math.sin(glow_timer * 1.5))
    
    title_x = SCREEN_WIDTH // 2 - title_font.render(title_string, True, (0,0,0)).get_width() // 2
    title_y = SCREEN_HEIGHT // 4

    # Blit multiple semi-translucent deep red surfaces offset around the title to simulate a neon aura
    for offset_x in range(-glow_radius, glow_radius + 1, 2):
        for offset_y in range(-glow_radius, glow_radius + 1, 2):
            if offset_x != 0 or offset_y != 0:
                glow_surface = title_font.render(title_string, True, (120, 0, 0))
                glow_surface.set_alpha(65)
                screen.blit(glow_surface, (title_x + offset_x, title_y + offset_y))

    # Render the primary, sharp foreground text layer in bright electric crimson
    title_main = title_font.render(title_string, True, (255, 30, 30))
    screen.blit(title_main, (title_x, title_y))

    # 4. Interactive Restart Button Setup
    button_width, button_height = 220, 55
    button_x = SCREEN_WIDTH // 2 - button_width // 2
    button_y = SCREEN_HEIGHT * 3 // 5
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    # Check if the player is hovering their mouse over the button boundaries
    is_hovered = button_rect.collidepoint(mouse_x, mouse_y)

    # Dynamic styling changes based on mouse focus states
    if is_hovered:
        button_color = (255, 40, 40)       # Vivid neon red on hover
        text_color = (20, 10, 20)           # Dark contrast text
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) # Swap cursor icon
    else:
        button_color = (40, 20, 25)         # Muted burgundy border outline
        text_color = (240, 200, 200)        # Soft tinted pink hue
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    # Draw the interactive UI card capsule elements
    pygame.draw.rect(screen, button_color, button_rect, border_radius=8)
    if not is_hovered:
        # Give the idle state a fine glowing neon structural bounding outline
        pygame.draw.rect(screen, (255, 50, 50), button_rect, width=2, border_radius=8)

    # Render and precisely center text labels into the visual capsule
    btn_text = button_font.render("RESTART", True, text_color)
    btn_text_x = button_rect.centerx - btn_text.get_width() // 2
    btn_text_y = button_rect.centery - btn_text.get_height() // 2
    screen.blit(btn_text, (btn_text_x, btn_text_y))

    # 5. Process Input Loops Without Blocking Window Controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) # Reset cursor standard behavior
            return "QUIT"
            
        # Route back to start screen if they press the Spacebar as a shortcut layout
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return "START_SCREEN"

    # Click interaction handler: checks if mouse button was activated inside the collision boundaries
    if is_hovered and mouse_clicked:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        return "START_SCREEN"

    # Maintain screen loop sequence
    return "game_over_SCREEN"
