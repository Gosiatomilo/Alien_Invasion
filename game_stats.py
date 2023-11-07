class GameStats:
    """Monitoring statistical data in the alien invasion game"""
    
    def __init__(self, ai_game):
        """Static data initialisation"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Starting the game "Alien invasion" in the active state
        self.game_active = False

        # High score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """Initialisation of statistical data that can change during the course of the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    