import sys
import pygame

class AlienInvasion:
    '''Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry'''

    def __init__(self):
        '''Inicjalizacja gry i utworzenie jej zasobów'''
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption('Inwacja Obcych')

        self.bg_color = (255,192,203)


    def run_game(self):
        '''Rozpoczęcie pętli głównej gry'''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()