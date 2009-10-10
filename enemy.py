# -*- coding: utf-8 -*-

import frametime, pygame, random, properties

class Enemy:
    enemy = pygame.image.load(properties.enemy_ship).convert()
    enemyrect = enemy.get_rect()
    cooldown_time = 0
    
    def __init__(self, where_spawn):
        self.enemyrect = self.enemy.get_rect()
        self.enemyrect.move_ip(where_spawn, 0)
        self.cooldown_time = 0
    
    def can_fire(self):
        diff_time = frametime.get_diff_time()
        self.cooldown_time += diff_time
        
        if self.cooldown_time > random.random() + 1:
            self.cooldown_time = 0
            return True
        else:
            return False
            
    def fire(self, bullet):
        if self.can_fire():
            bullet.enemy_fire(self.enemyrect.midbottom)
