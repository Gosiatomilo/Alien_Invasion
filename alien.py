import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Klasa przedstawiająca pojedyńczego obcego i zdefiniowanie jego połozenia początkowego'''
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Wczytanie obrazu obcego i zdefiniowanie atrybutu rect 
        self.image = pygame.image.load('/Users/malgorzatatomilo/Documents/GitHub/InwazjaObcych/ufo-4778062_640.bmp')
        self.rect = self.image.get_rect()
        # Umieszczenie nowego obcego w poblizu lewego górnego rogu ekranu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Przechowywanie dokładnego poziomego połozenia obcego 
        self.x = float(self.rect.x)

    def update(self):
        '''Przeunięcie obcego w prawo'''
        self.x += self.settings.alien_speed
        self.rect.x = self.x


    def check_edges(self):
        '''Zwraca wartość True, jeśli obcy znajduję się przy krawędzi ekranu'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
    def update(self):
        '''Przesunięcie obcego w prawo lub lewo'''
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        
        self.rect.x = self.x

