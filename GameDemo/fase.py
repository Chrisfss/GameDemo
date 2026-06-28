import pygame

from GameDemo.entity import Entity
from GameDemo.entityFactory import EntityFactory
from GameDemo.entityMediator import EntityMediator
from GameDemo.player import Player
from GameDemo.enemy import Enemy
from GameDemo.Const import EVENT_ENEMY, SPAWN, EVENT_TIMEOUT, TIMEOUT_STEP


class Fase:

    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.timeout = 20000
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('fase'))
        self.entity_list.append(EntityFactory.get_entity('player'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    skill = ent.skill()
                    if skill is not None:
                        self.entity_list.append(skill)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('enemy'))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        return "WIN"

                loseCondition = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        loseCondition = True

                if loseCondition == False:
                    return 'GAMEOVER'

            EntityMediator.collisionverifier(entity_list=self.entity_list)
            EntityMediator.lifeverifier(entity_list=self.entity_list)

            pygame.display.flip()
        pass
