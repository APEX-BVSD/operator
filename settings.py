"""
Contains settings for the game.
Month Year
First Last
First Last 
First Last 
"""


SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
FPS: int = 60

GAME_TITLE: str = "SMOOTH OPERATOR"

# Arbitrary alignment of UI elements
BOTTOM_LIST_TOP_LEFT: list[int] = [(SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 6), 6 * (SCREEN_HEIGHT / 8)]
SIDE_LIST_TOP_LEFT: list[int] = [SCREEN_WIDTH / 20, SCREEN_HEIGHT / 8]