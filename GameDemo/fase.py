import pygame

from GameDemo.entity import Entity
from GameDemo.entityFactory import EntityFactory


class Fase:

    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.timeout = 20000
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('fase'))
        self.entity_list.append(EntityFactory.get_entity('player'))


    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
