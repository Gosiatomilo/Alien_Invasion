import pygame

class Ship:
    '''klasa przeznaczona do zarządzania statkiem kosmicznym'''

    def __init__(self, ai_game):
            '''Inicjacja statku kosmicznego i jego połozenie'''
            

            self.screen = ai_game.screen
            self.settings = ai_game.settings
            self.screen_rect = ai_game.screen.get_rect()

            self.image = pygame.image.load('/Users/malgorzatatomilo/Documents/GitHub/InwazjaObcych/rocket-147466_640.bmp')
            self.rect = self.image.get_rect()
            

            self.rect.midbottom = self.screen_rect.midbottom
            self.x = float(self.rect.x)

            self.moving_right = False
            self.moving_left = False

    def update(self):
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x += self.settings.ship_speed
            if self.moving_left and self.rect.left >0 :
                self.x -= self.settings.ship_speed

            self.rect.x = self.x

    def blitme (self):
          self.screen.blit(self.image,self.rect)
            
    def center_ship(self):
          '''Umieszczenie statku na środku przy dolnej krawędzi ekranu'''
          self.rect.midbottom = self.screen_rect.midbottom
          self.x = float(self.rect.x)

