import pygame
from pygame import Surface


class GameOver:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/loseimage.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


            self.window.blit(self.surf, self.rect)
            pygame.display.flip()