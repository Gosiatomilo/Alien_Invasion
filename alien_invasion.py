import sys
from time import sleep
import pygame
from settings import Settings
from game_starts import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button



class AlienInvasion:
    '''Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania gry'''

    def __init__(self):
        '''Inicjalizacja gry i utworzenie jej zasobów'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('Inwacja Obcych')
        self.stats = GameStats(self)
        self.ship = Ship(self)
# Utworzenie grupy pocisków 
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self, "Gra")

    def run_game(self):
        '''Rozpoczęcie pętli głównej gry'''
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._updete_bullets()
                self._updete_aliens()
            self._update_screen()
            

    def _check_events(self):
        '''Reakcja na zdarzenia generowane przez mysz i klawiature'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
                    
    def _check_play_button(self, mouse_pos):
        '''Rozpoczęcie nowej gry po kliknięciu przysisku przez uzytkownika'''
        button_cliked = self.play_button.rect.collidepoint(mouse_pos)
        if button_cliked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            # Wyzerowanie danych statystycznych gry
            self.stats.reset_stats()
            self.stats.game_active = True
            # Usunięcie zawarotści list aliens i bullets
            self.aliens.empty()
            self.bullets.empty()
            # Utworzenie nowej floty i wyśrodkowanie statku
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)


    def _check_keydown_events(self,event):
        '''Reakcja na naciśnięcie klawisza'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
        
    
    def _check_keyup_events(self,event):
        '''Reakcja na zwolnenie klawisza'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''Utworzenie nowego pocisku i dodanie go do grupy pocisków'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _updete_bullets(self):
        '''Uaktualnianie połozenia przycisków i susnięcie tych nie widocznych na ekranie'''
        # Uaktualnianie połozenia przycisków
        self.bullets.update()
        
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        # Sprawdzenie, czy którykolwiek pocisk trafił obcego
        # Jeśli takusuwamy pocisk i obcego 
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
        # Usunięcie pocisków, które zanjdują się poza ekranem
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        '''Reakcja na kolizje między pociskiem i obcym'''
        # Usunięcie wszystkich pociskow i obcych, mi≥ędzy którymi doszło do kolizji
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()


    def _updete_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        # Wykrywanie kolizji między obcym i statkiem
        if pygame.sprite.spritecollideany (self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()



    def _create_fleet(self):
        '''Utworzenie pełnej floty obcych'''
        # Utworzenie obcego
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        availble_space_x = self.settings.screen_width - (2* alien_width)
        numer_aliens_x = availble_space_x // (2 * alien_width)
        # Ustalenie, ile rzędów obcych zmieści się na ekranie
        ship_height = self.ship.rect.height
        availble_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = availble_space_y // (2 * alien_height)
        # Utworzenie pełnej floty obcych 
        for row_number in range(number_rows):
            for alien_number in range(numer_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien ( self, alien_number, row_number):
        '''Utworzenie obcego i umieszczenie go w rzędzie'''
        alien = Alien(self)
        alien_width , alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 *alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        '''Odpowiednia rekcja, gdy obcy dotrze do krawędzi ekranu'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''Przesnięcie całej floty obcych w dół i zmiana kierunku, w którym się ona porusza'''
        for alien in self.aliens.sprites():
            alien.rect.y +=self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        '''Sprawdzenie, czy którykolwiek obcy dotarł do dolenej krawędzi ekranu'''
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Tak samo jak w przypadku zdarzenia statku z obcymi
                self._ship_hit()
                break
        

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color) 
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # Wyświetlenie przycisku tylko wtedy, gdy gra jest nieaktywna
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _ship_hit(self):
        '''Reakcja na uderzenie obcego w statek'''
        # Zmiejszenie wartości przechowywanej w ships_left
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            # Usunięcie zawartości list aliens i bullets 
            self.aliens.empty()
            self.bullets.empty()
            # Utworzenie nowej floty i wyśrodkowanie statku
            self._create_fleet()
            self.ship.center_ship()
            # Pauza 
            sleep(0.5)
        else:
            # Uruchomienie gry w stanie aktywnym
            self.game_active = False
            pygame.mouse.set_visible(True)
         

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()