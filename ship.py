import pygame
class Ship:
    '''klasa przeznaczona do zarządzania statkiem kosmicznym'''

    def __init__(self, ai_game):
            '''Inicjacja statku kosmicznego i jego połozenie'''

            self.screen = ai_game.screen
            self.screen_rect = ai_game.screen.get_rect()

            self.image = pygame.image.load('/Users/malgorzatatomilo/Documents/GitHub/InwazjaObcych/rocket-147466_640.bmp')
            self.rect = self.image.get_rect()

            self.rect.midbottom = self.screen_rect.midbottom

    def blitme (self):
          self.screen.blit(self.image,self.rect)
            

