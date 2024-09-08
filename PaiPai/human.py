import pygame

class Human():
    def __init__(self, pi_game):
        self.screen = pi_game.screen
        self.screen_rect = pi_game.screen.get_rect()
        self.settings = pi_game.settings
        
        self.image = pygame.image.load('images/human.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.human_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.human_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.human_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.human_speed
        self.rect.x = self.x
        self.rect.y = self.y
        
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)