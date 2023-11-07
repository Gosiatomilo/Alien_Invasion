class Settings:
    """A class designed to hold all game settings"""

    def __init__(self):
        """Initialise game settings"""
        # Rocket settings
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (242, 212, 215)

        # Spacecraft settings
        self.ship_limit = 3

        # Arrangements for missiles
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # Easy change of game speed
        self.speedup_scale = 1.1

        # Easy change to the number of points awarded for shooting a stranger
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50


    def increase_speed(self):
        """Changing the speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
