from GameDemo.Const import ENTITY_SPEED
from GameDemo.entity import Entity


class EnemySkill(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]