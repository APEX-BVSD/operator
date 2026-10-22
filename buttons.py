from collections import abc

import pygame


class TextBox:
    def __init__(
        self,
        image_path: str | pygame.Surface,
        text: str,
        size: tuple[int, int],
        pos: tuple[int, int],
        font: str,
        ljustify: bool | None = None,
    ):
        self.size = size
        self.text = text
        self.image: pygame.Surface
        if type(image_path) == str:
            self.image = pygame.transform.scale(
                pygame.image.load(image_path), (self.size[0], self.size[1])
            )
        elif type(image_path) == pygame.Surface:
            self.image = image_path
        self.pos = pos
        pygame.font.init()
        self.f: pygame.Font = pygame.Font()

        self._margin_w: int = (self.size[0] - self.f.size(self.text)[0]) // 4
        self._margin_h: int = 4 * ((self.size[1] - self.f.size(self.text)[1]) // 8)

        if ljustify:
            self._margin_w = self.f.size(self.text[0])[0]
            self._margin_h = self._margin_w

        try:
            self.f = pygame.Font(
                font, size=int((self.size[0] - self._margin_w) / len(self.text))
            )
            if ljustify:
                self.f = pygame.Font(font, size=self.size[1] - self._margin_h)
        except:
            self.f = pygame.Font(size=42)

        self.image.blit(
            self.f.render(self.text, True, (255, 255, 255)),
            pygame.Rect(
                self._margin_w,
                self._margin_h,
                self.f.size(self.text)[0],
                self.f.size(self.text)[1],
            ),
        )  # FIXME: uncentered


class Button(TextBox):
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
