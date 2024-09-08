import pygame
from pygame.sprite import Sprite
import math

class Attac(Sprite):
    
    def __init__(self, pi_game):
        super().__init__()
        self.screen = pi_game.screen
        self.settings = pi_game.settings
        self.color = self.settings.attacs_color
        
        self.rect = pygame.Rect(0,0, self.settings.attacs_width, self.settings.attacs_height)
        self.rect.midtop = pi_game.human.rect.midtop
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.direction_x = 0.0  
        self.direction_y = 0.0
        
    def update(self):
        self.x += self.direction_x * self.settings.attacs_speed
        self.y += self.direction_y * self.settings.attacs_speed 
        self.rect.x = self.x
        self.rect.y = self.y

    def set_direction(self, target_x, target_y):
        self.x = self.rect.x  # Обновляем начальные координаты
        self.y = self.rect.y
        
        delta_x = target_x - self.x
        delta_y = target_y - self.y
        distance = math.sqrt(delta_x**2 + delta_y**2)
        
        if distance != 0:  # Проверяем деление на ноль
            self.direction_x = delta_x / distance
            self.direction_y = delta_y / distance
            
    def draw_attacs(self):
        pygame.draw.rect(self.screen, self.color, self.rect)