import sys
import pygame
from settings import Settings
from ship import Ship

#poetry 
class AlienInvasion:
    '''Overall Class To Manage The Game Assets And Behaviour'''

    def __init__(self):
        '''Initializes The Game,And Create Game Resources'''
        pygame.init()
        self.settings = Settings()


        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)

        #setting the bg color
        self.bg_color = self.settings.bg_color
    
    def run_game(self):
        '''Start The Main Loop For The Game.'''
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()

    def _check_events(self):
        '''respond to keypress and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #move the ship to the right
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
            
    def _update_screen(self):
        '''update images on the screen and flip to the new screen '''
        self.screen.fill(self.bg_color)
        self.ship.blitme()

        #making the most recently drawn screen visible 
        pygame.display.flip()

if __name__ == '__main__':
    #making and game instance to run it
    ai = AlienInvasion()
    ai.run_game()        