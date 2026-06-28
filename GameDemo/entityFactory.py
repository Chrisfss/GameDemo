from random import randint, random

from GameDemo.Const import WIN_HEIGHT, WIN_WIDTH
from GameDemo.background import Background
from GameDemo.enemy import Enemy
from GameDemo.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position =( 0, 0)):

        match entity_name:
            case 'fase':
                list_background = []
                for i in range(7):
                    list_background.append(Background(f'fase{i}', (0,0)))
                    list_background.append(Background(f'fase{i}', (WIN_WIDTH, 0)))
                return list_background
            case 'player':
                return Player('player', (20, 400))
            case 'enemy':
                return Enemy('enemy', (WIN_WIDTH +10 , 400))

