import pygame

class PlaceholderPlaceholder():
    hitbox: pygame.Rect = pygame.Rect(0,
                                       0,
                                       100, 100
    )
    position: tuple = (0, 0)

class Placeholder1(PlaceholderPlaceholder):
    image: pygame.Surface = pygame.image.load("placeholder1.png")
    
class Placeholder2(PlaceholderPlaceholder):
    image: pygame.Surface = pygame.image.load("placeholder2.png")

class Placeholder3(PlaceholderPlaceholder):
    image: pygame.Surface = pygame.image.load("placeholder3.png")
