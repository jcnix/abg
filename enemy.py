# -*- coding: utf-8 -*-

import frametime, pygame, random, properties

class Enemy(pygame.sprite.DirtySprite):
    enemy = pygame.image.load(properties.enemy_ship).convert_alpha()
    enemyrect = enemy.get_rect()
    cooldown_time = 0
    
    def __init__(self, where_spawn):
        pygame.sprite.Sprite.__init__(self)
        self.enemyrect = self.enemy.get_rect()
        self.enemyrect.move_ip(where_spawn, 0)
        self.cooldown_time = 0
    
    def update(self, bullet):
        self.fire(bullet) #fires if possible
        move_speed = [0, 150]
        move_speed = frametime.modify_speed(move_speed)
        self.enemyrect = self.enemyrect.move(move_speed)
    
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
