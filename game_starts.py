class GameStats:
    '''Monitorowanie danych statystycznych w grze "Inwacja Obcych"'''
    
    def __init__(self, ai_game):
        '''Inicjalizacja danych statyctycznych'''
        self.settings = ai_game.settings
        self.reset_stats()
        # Uruchomienie gry "Inwazja obcych" w stanie aktywnym
        self.game_active = False 
        self.high_score = 0

    def reset_stats(self):
        '''Inicjalizacja danych statystycznych, które mogą zmieniać się w trakcie gry'''
        self.ships_left = self.settings.ship_limit
        self.score = 0

    