import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Klasa przedstawiająca pojedyńczego obcego i zdefiniowanie jego połozenia początkowego'''
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        # Wczytanie obrazu obcego i zdefiniowanie atrybutu rect 
        self.image = pygame.image.load('/Users/malgorzatatomilo/Documents/GitHub/InwazjaObcych/ufo-4778062_640.bmp')
        self.rect = self.image.get_rect()
        # Umieszczenie nowego obcego w poblizu lewego górnego rogu ekranu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Przechowywanie dokładnego poziomego połozenia obcego 
        self.x = float(self.rect.x)

