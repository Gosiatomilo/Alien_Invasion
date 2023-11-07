import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class designed to manage a spacecraft"""

    def __init__(self, ai_game):
        """Spacecraft initiation and positioning"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load(
            './image/rocket.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

            # Update rect object from self.x
            self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
            
    def center_ship(self):
        """Placing the ship in the centre at the bottom edge of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
