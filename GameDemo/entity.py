from abc import ABC, abstractmethod

import pygame

from GameDemo.Const import ENTITY_LIFE, ENTITY_SPEED, ENTITY_DAMAGE


class Entity(ABC):
    def __init__(self, name, position):
        self.name = name
        self.surf = pygame.image.load('./assets/' + name +'.png').convert_alpha()
        self.rect = self.surf.get_rect(topleft=position)
        self.speed = 0
        self.damage = ENTITY_DAMAGE[self.name]
        self.life = ENTITY_LIFE[self.name]
        self.ldamage = 'None'


    @abstractmethod
    def move(self, ):
        pass
