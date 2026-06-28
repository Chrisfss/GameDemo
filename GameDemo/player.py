import pygame

from GameDemo.Const import WIN_WIDTH, ENTITY_SPEED, SKILL_DELAY
from GameDemo.entity import Entity
from GameDemo.playerSkills import PlayerSkill


class Player(Entity):

    def __init__(self, name:str, position: tuple):
        super().__init__(name, position)
        self.skill_delay = SKILL_DELAY[self.name]

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_a] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_d] and self.rect.right < WIN_WIDTH - 70:
            self.rect.centerx += ENTITY_SPEED[self.name]

    def skill(self):
        self.skill_delay -= 1
        if self.skill_delay == 0:
            self.skill_delay = SKILL_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_LSHIFT]:
                return PlayerSkill(name=f'{self.name}Skill', position=(self.rect.centerx, self.rect.centery))