import pygame
from pygame import Surface, Rect

from GameDemo.Const import CONTROLS, WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE


class controlsWindow:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/menu.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            self.window.blit(self.surf, self.rect)

            for i in range(len(CONTROLS)):
                self.control_text(40,CONTROLS[i],COLOR_WHITE,((WIN_WIDTH / 2), (WIN_HEIGHT / 3) + 70 * i )
                )

            pygame.display.flip()


    def control_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        from pygame import Font
        text_font: Font = pygame.font.SysFont(name="lucidasans", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)