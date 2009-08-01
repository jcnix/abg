# -*- coding: iso-8859-1 -*-
import sys, pygame, frametime
from enemy import Enemy

class Bullet:
    bullet = pygame.image.load("res/bullet.png").convert()
    bulletrect = bullet.get_rect()
    bulletrects = []

    def fire(self, pshiprect):       
        self.bulletrect = self.bullet.get_rect()
        self.bulletrect.move_ip(pshiprect)
        self.bulletrects.append(self.bulletrect)
                
    def move(self, screen, enemy):
        if len(self.bulletrects) > 0:
            bullet_speed = [0, -750]
            bullet_speed = frametime.modify_speed(bullet_speed)
            enemies = enemy.getEnemies()
            
            to_delete = []
            
            for i in range(len(self.bulletrects)):
                self.bulletrects[i] = self.bulletrects[i].move(bullet_speed)
                screen.blit(self.bullet, self.bulletrects[i])
                
                #If bullet goes off the top of the screen
                if self.bulletrects[i].top < 0:
                    to_delete.append(i)
                
                #If bullet hits an enemy
                collision = self.bulletrects[i].collidelist(enemies)
                if collision != -1:
                    to_delete.append(i)
                    enemy.remove(collision)
                    
            for x in to_delete:
                del self.bulletrects[x]
                
