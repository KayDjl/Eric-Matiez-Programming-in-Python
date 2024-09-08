import pygame
from pygame import sprite
from pygame.sprite import Sprite

class Monster(Sprite):
    """Инициализация монстра и устоновка его позиции"""
    
    def __init__(self, pi_game):
        super().__init__()
        self.screen = pi_game.screen
        self.image = pygame.image.load('images/monster.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.monster_width, self.monster_height = self.rect.size
        self.x_pos = self.monster_width // 2
        self.y_pos = self.monster_height // 2 
        
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        