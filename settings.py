class Settings:
    '''klasa przeznaczona do przechowywania wszystkich ustawiań gry'''

    def __init__(self):
        '''inicjalizacja ustawień gry'''
# ustawienia dotyczące rakiety 
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (242,212,215)
        self.ship_speed = 1.5
# ustwienia dotyczące pocisków
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
# ustawienia dotyczące kosmitów
        self.alien_speed = 0.3
        self.fleet_drop_speed = 10
        self.fleet_direction = 1