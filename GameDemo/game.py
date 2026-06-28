import pygame

from GameDemo.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTIONS, CONTROLES
from GameDemo.fase import Fase
from GameDemo.gameOver import GameOver
from GameDemo.menu import Menu
from GameDemo.win import Win


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTIONS[0]:
                fase = Fase(self.window, 'Fase')
                fase_result = fase.run()
                if fase_result == "WIN":
                    win = Win(self.window)
                    win.run()
                if fase_result == "GAMEOVER":
                    lose = GameOver(self.window)
                    lose.run()

            if menu_return == MENU_OPTIONS[2]:
                pygame.quit()
                quit()
