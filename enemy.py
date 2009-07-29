# -*- coding: utf-8 -*-
import sys, pygame

class Enemy:
    enemy = pygame.image.load("res/enemy.png").convert()
    enemyrect = enemy.get_rect()
    enemies = []

    def init(self, screen):
        self.enemyrect = self.enemy.get_rect()
        self.enemies.append(self.enemyrect)
        self.enemyrect.move_ip(400, 300)
        screen.blit(self.enemy, self.enemyrect)
        
    def getEnemies(self):
        return self.enemies
