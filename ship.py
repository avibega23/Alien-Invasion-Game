import pygame

class Ship:
    '''A Classs TO Manage The Ship'''

    def __init__(self,ai_game):
        '''Initiliaze the ship and set its starting position'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        '''Load The Image and get its rect'''
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        '''starts each ship at the midbottom'''
        self.rect.midbottom = self.screen_rect.midbottom

        #movement flag
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        '''draw the ship at his current location'''
        self.screen.blit(self.image,self.rect)