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

PIX_PER_PT: float = 1.5
#scuffed font rendering workaround

class Button(TextBox):
    function: Callable
    click_bb: Rect = pygame.Rect(0, 0, 0, 0)

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
        self.function = callback
        self.size = size
        self.click_bb = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.text = text
        self.image = pygame.transform.scale(
            pygame.image.load(image_path), (self.size[0], self.size[1])
        )
        pygame.font.init()
        f: pygame.Font = pygame.Font()
        try:
            f = pygame.Font(font, size=int(self.size[0] * PIX_PER_PT / len(self.text)))
        except:
            f = pygame.Font(size=42)
        _margin_w: int = (self.size[0] - f.size(self.text)[0]) // 2
        _margin_h: int = (self.size[1] - f.size(self.text)[1]) // 2
        self.image.blit(f.render(self.text, True, (255, 255, 255)), (_margin_w, _margin_h))
