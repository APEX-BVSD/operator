from collections import abc

import pygame


class TextBox:
    image: pygame.Surface = None
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
        f: pygame.Font = pygame.Font()


        _margin_w: int = (self.size[0] - f.size(self.text)[0]) // 2
        _margin_h: int = (self.size[1] - f.size(self.text)[1]) // 2

        try:
            f = pygame.Font(font, size=int((self.size[0] - _margin_w)/ len(self.text)))
        except:
            f = pygame.Font(size=42)
        self.image.blit(f.render(self.text, True, (255, 255, 255)), (_margin_w, _margin_h)) # FIXME: uncentered


class Button(TextBox):
    function: abc.Callable
    click_bb: pygame.Rect = pygame.Rect(0, 0, 0, 0)

    def __init__(
        self,
        callback: abc.Callable,
        image_path: str,
        text: str,
        size: tuple[int, int],
        pos: tuple[int, int],
        font: str | None = None,
    ):
        self.function = callback
        self.size = size
        self.click_bb = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.text = text
        self.pos = pos
        self.image = pygame.transform.scale(
            pygame.image.load(image_path), (self.size[0], self.size[1])
        )
        TextBox.__init__(self, image_path, text, size, pos, font)
