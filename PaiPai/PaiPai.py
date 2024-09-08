import sys

import pygame
import random

from settings import Settings
from human import Human
from Attacs import Attac
from Monsteres import Monster

class Paipai():
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_widht, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('PaiPai')
        self.human = Human(self)
        self.attacs = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()
        self._update_monsters()
        
    def run_game(self):
        while True:
            self._check_ivent()
            self.human.update()
            self._update_screen()
            self._update_attacs()
            

    def _check_ivent(self):
        for ivent in pygame.event.get():
            if ivent.type == pygame.QUIT:
                sys.exit()
            elif ivent.type == pygame.KEYDOWN:
                self._check_keydown_event(ivent)
            elif ivent.type == pygame.KEYUP:
                self._check_keyup_event(ivent)
            elif ivent.type == pygame.MOUSEBUTTONDOWN and ivent.button == 1:
                self._fire_attacs(ivent.pos)
                    
    def _check_keydown_event(self, ivent):
        if ivent.key == pygame.K_d:
            self.human.moving_right = True
        if ivent.key == pygame.K_a:
            self.human.moving_left = True
        if ivent.key == pygame.K_w:
            self.human.moving_up = True
        if ivent.key == pygame.K_s:
            self.human.moving_down = True
            
    def _check_keyup_event(self, ivent):
        if ivent.key == pygame.K_d:
            self.human.moving_right = False
        if ivent.key == pygame.K_a:
            self.human.moving_left = False
        if ivent.key == pygame.K_w:
            self.human.moving_up = False
        if ivent.key == pygame.K_s:
            self.human.moving_down = False
            
    def _fire_attacs(self, target_pos):
        new_attacs = Attac(self)
        new_attacs.set_direction(*target_pos)
        self.attacs.add(new_attacs)
                    
    def _update_attacs(self):
        self.attacs.update()
        for attac in self.attacs.copy():
            if attac.rect.bottom <= 0:
                self.attacs.remove(attac)
            elif attac.rect.left <= 0:
                self.attacs.remove(attac)
            elif attac.rect.top > self.screen_rect.bottom:
                self.attacs.remove(attac)
            elif attac.rect.right > self.screen_rect.right:
                self.attacs.remove(attac)
                
    def _is_position_valid(self, x, y, width, height):
        for monster in self.monsters:
            if (abs(monster.rect.x - x) < width) and (abs(monster.rect.y - y) < height):
               return False
        return True

    def _update_monsters(self):
        monster = Monster(self)
        monster_width, monster_height = monster.rect.size
        for _ in range(self.settings.monsters_add):
            random_x = random.randint(0, self.settings.screen_widht - monster_width)
            random_y = random.randint(0, self.settings.screen_height - monster_height)
            if self._is_position_valid(random_x, random_y, monster_width, monster_height):
                    self._create_monsters(random_x, random_y)
                    

    def _create_monsters(self, random_x, random_y):
        monster = Monster(self)
        monster.x = random_x
        monster.rect.x = random_x
        monster.y = random_y
        monster.rect.y = random_y
        self.monsters.add(monster)
        
                
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.human.blitme()
        for attac in self.attacs.sprites():
            attac.draw_attacs()
        self.monsters.draw(self.screen)
        pygame.display.flip()
        
if __name__ == '__main__':
    pi = Paipai()
    pi.run_game()
