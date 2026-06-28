import pygame

from GameDemo.Const import WIN_WIDTH, ENTITY_SPEED, SKILL_DELAY
from GameDemo.enemySkills import EnemySkill
from GameDemo.entity import Entity

class Enemy(Entity):

    def __init__(self, name:str, position: tuple):
        super().__init__(name, position)
        self.skill_delay = SKILL_DELAY[self.name]

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def skill(self):
        self.skill_delay -= 1
        if self.skill_delay == 0:
            self.skill_delay = SKILL_DELAY[self.name]
            return EnemySkill(name=f'{self.name}Skill', position=(self.rect.centerx, self.rect.centery))