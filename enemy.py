# -*- coding: utf-8 -*-
import sys, pygame

class Enemy:
    enemy = pygame.image.load("res/enemy.png").convert()
    enemyrect = enemy.get_rect()
    enemies = []
    
    def create(self):
        self.enemyrect = self.enemy.get_rect()
        self.enemies.append(self.enemyrect)
        self.enemyrect.move_ip(400, 300)

    def move(self, screen):
        if len(self.enemies) > 0:
            screen.blit(self.enemy, self.enemies[0])
        
    def getEnemies(self):
        return self.enemies
        
    def remove(self, index):
        del self.enemies[index]
