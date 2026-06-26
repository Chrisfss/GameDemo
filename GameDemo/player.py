import pygame

from GameDemo.Const import WIN_WIDTH, ENTITY_SPEED
from GameDemo.entity import Entity

class Player(Entity):

    def __init__(self, name:str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_a] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_d] and self.rect.right < WIN_WIDTH - 70:
            self.rect.centerx += ENTITY_SPEED[self.name]
        # if pressed_key[pygame.K_SPACE] and self.rect.top > 340:
