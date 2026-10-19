from collections import abc

import pygame


class TextBox:
    image: Surface = None
    text: str = ""
    size: tuple[int, int] = (0, 0)
    pos: tuple[int, int] = (0, 0)

    def __init__(
        self,
        image_path: str,
        text: str,
        size: tuple[int, int],
        pos: tuple[int, int],
        font: str,
    ):
        self.size = size
        self.text = text
        self.image = pygame.transform.scale(
            pygame.image.load(image_path), (self.size[0], self.size[1])
        )
        pygame.font.init()
        try:
            f = pygame.Font(font, size=42)
            self.image = f.render(self.text, True, (255, 255, 255))
        except:
            f = pygame.Font(size=42)
            self.image = f.render(self.text, True, (255, 255, 255))


class Button(TextBox):
    _function: Callable = print("Default button behavior")

    def __init__(
        self,
        callback: Callable,
        image_path: str,
        text: str,
        size: tuple[int, int],
        pos: tuple[int, int],
        font: str | None = None,
    ):
        TextBox.__init__(self, image_path, text, size, pos, font)
        self._function = callback
        self.size = size
        self.text = text
        self.image = pygame.transform.scale(
            pygame.image.load(image_path), (self.size[0], self.size[1])
        )
        pygame.font.init()
        try:
            f = pygame.Font(font, size=42)
            self.image = f.render(self.text, True, (255, 255, 255))
        except:
            f = pygame.Font(size=42)
            self.image = f.render(self.text, True, (255, 255, 255))
