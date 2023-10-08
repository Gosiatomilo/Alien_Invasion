class Settings:
    '''klasa przeznaczona do przechowywania wszystkich ustawiań gry'''

    def __init__(self):
        '''inicjalizacja ustawień gry'''
# ustawienia dotyczące rakiety 
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (242,212,215)
# ustawienia dotyczące ststk kosmicznego 
        self.ship_limit = 3
# ustwienia dotyczące pocisków
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
# ustawienia dotyczące kosmitów
        self.fleet_drop_speed = 10
# Łatwa zmiana szybkości gry
        self.setup_scale = 1.1 
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Inicjalizacja ustawień, które ulegają zmianie w trakcie gry'''
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = 1

    def increase_speed(self):
        '''Zmiana ustawień dotyczących szybkości'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
