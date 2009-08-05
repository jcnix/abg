# -*- coding: utf-8 -*-
import sys, pygame, frametime
import random

class Enemy:
    enemy = pygame.image.load("res/enemy.png").convert()
    enemyrect = enemy.get_rect()
    enemies = []
    
    def create(self):
        #range that the current player ship can shoot
        where_spawn = random.randint(1, 800-50)
        
        self.enemyrect = self.enemy.get_rect()
        self.enemies.append(self.enemyrect)
        self.enemyrect.move_ip(where_spawn, 0)

    def move(self, screen):
        if frametime.can_create_enemy():
            self.create()
            
        if len(self.enemies) > 0:
            for i in range(len(self.enemies)):
                screen.blit(self.enemy, self.enemies[i])
        
    def getEnemies(self):
        return self.enemies
        
    def remove(self, index):
        del self.enemies[index]
