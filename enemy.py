# -*- coding: utf-8 -*-

import frametime, pygame

class Enemy:
    enemy = pygame.image.load("res/enemy.png").convert()
    enemyrect = enemy.get_rect()
    cooldown_time = 0
    to_cooldown = 1
    
    def __init__(self, where_spawn):
        self.enemyrect = self.enemy.get_rect()
        self.enemyrect.move_ip(where_spawn, 0)
    
    def can_fire(self):
        global cooldown_time
        global time_to_cooldown
        
        cooldown_time = frametime.can_enemy_fire(cooldown_time)
        if cooldown_time > to_cooldown:
            return True
        else:
            return False
