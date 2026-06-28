import pygame
from pygame import Surface, Font, Rect

from GameDemo.Const import COLOR_GOLDEN, WIN_WIDTH, WIN_HEIGHT


class Win:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/winimage.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.text(100, "VICTORY!", COLOR_GOLDEN, ((WIN_WIDTH / 2), (WIN_HEIGHT / 4) ))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            pygame.display.flip()

    def text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="lucidasans", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
