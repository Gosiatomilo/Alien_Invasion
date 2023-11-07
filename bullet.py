import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class designed to manage the missiles fired by a ship"""
    def __init__(self, ai_game):
        """Creation of a projectile object in the current position of the ship"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings 
        self.color = self.settings.bullet_color

        # Create a projectile rectangle at point (0,0) and then define a suitable position for it
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height) 
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Moving a bullet across the screen"""
        # Updating the bullet position
        self.y -= self.settings.bullet_speed
        # Updating the position of the projectile rectangle
        self.rect.y = self.y

    def draw_bullet(self):
        """Displaying the projectile on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
