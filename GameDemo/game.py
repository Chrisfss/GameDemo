import pygame

from GameDemo.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTIONS
from GameDemo.menu import Menu
class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTIONS[2]:
                pygame.quit()
                quit()
