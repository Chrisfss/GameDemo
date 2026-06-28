from GameDemo.Const import WIN_WIDTH
from GameDemo.enemy import Enemy
from GameDemo.enemySkills import EnemySkill
from GameDemo.entity import Entity
from GameDemo.player import Player
from GameDemo.playerSkills import PlayerSkill


class EntityMediator:

    @staticmethod
    def windowcollisionverifier(ent: Entity):

        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.life = 0

        elif isinstance(ent, PlayerSkill):
            if ent.rect.left >= WIN_WIDTH:
                ent.life = 0

        elif isinstance(ent, EnemySkill):
            if ent.rect.right <= 0:
                ent.life = 0


    @staticmethod
    def entitycollisionverifier(ent1, ent2):

        if ent1.rect.colliderect(ent2.rect):

            validcolision = (
                (Enemy, PlayerSkill),
                (PlayerSkill, Enemy),
                (Player, EnemySkill),
                (EnemySkill, Player),
            )

            if (type(ent1), type(ent2)) in validcolision:


                ent1.life -= ent2.damage
                ent2.life -= ent1.damage

                ent1.ldamage = ent2.name
                ent2.ldamage = ent1.name


    @staticmethod
    def collisionverifier(entity_list: list[Entity]):

        for i in range(len(entity_list)):
            ent1 = entity_list[i]

            EntityMediator.windowcollisionverifier(ent1)

            for j in range(i + 1, len(entity_list)):
                ent2 = entity_list[j]

                EntityMediator.entitycollisionverifier(ent1, ent2)


    @staticmethod
    def lifeverifier(entity_list: list[Entity]):

        entity_list[:] = [ent for ent in entity_list if ent.life > 0]