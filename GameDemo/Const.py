import pygame

COLOR_PURPLE = (163, 73, 164)
COLOR_WHITE = (255, 255, 255)
COLOR_GOLDEN = (212, 175, 55)

WIN_WIDTH = 900
WIN_HEIGHT = 506

MENU_OPTIONS = ["Jogar",
                "Controles",
                "Sair"
]
CONTROLS = ["WASD PARA MOVER",
            "LSHIFT PARA ATIRAR",
            "ESC PARA SAIR",
             ]
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'fase0': 2,
    'fase1': 2.5,
    'fase2': 3,
    'fase3': 3.5,
    'fase4': 4,
    'fase5': 4.5,
    'fase6': 5,
    'player': 3,
    'playerSkill': 20,
    'enemy': 4,
    'enemySkill':10
}
ENTITY_LIFE = {
    'fase0': 1,
    'fase1': 1,
    'fase2': 1,
    'fase3': 1,
    'fase4': 1,
    'fase5': 1,
    'fase6': 1,
    'fase7': 1,
    'fase8': 1,
    'menu': 1,
    'player': 200,
    'playerSkill': 1,
    'enemy': 300,
    'enemySkill':1
}
SKILL_DELAY = {
    'enemy': 60,
    'player': 15
}
ENTITY_DAMAGE = {
    'fase0': 0,
    'fase1': 0,
    'fase2': 0,
    'fase3': 0,
    'fase4': 0,
    'fase5': 0,
    'fase6': 0,
    'fase7': 0,
    'fase8': 0,
    'menu': 0,
    'player': 1,
    'playerSkill': 50,
    'enemy': 300,
    'enemySkill':30
}
SPAWN= 1500
TIMEOUT_STEP = 100