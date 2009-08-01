# -*- coding: iso-8859-1 -*-
import sys, pygame, enemy, frametime

class Bullet:
    bullet = pygame.image.load("res/bullet.png").convert()
    bulletrect = bullet.get_rect()
    bulletrects = []

    def fire(self, pshiprect):       
        self.bulletrect = self.bullet.get_rect()
        self.bulletrect.move_ip(pshiprect)
        self.bulletrects.append(self.bulletrect)
                
    def move(self, screen, enemies):
        bullet_speed = [0, -750]
        bullet_speed = frametime.modify_speed(bullet_speed)
        
        to_delete = []
        
        for i in range(len(self.bulletrects)):
            self.bulletrects[i] = self.bulletrects[i].move(bullet_speed)
            screen.blit(self.bullet, self.bulletrects[i])
            
            #If bullet goes off the top of the screen
            if self.bulletrects[i].top < 0:
                to_delete.append(i)
            
            collision = self.bulletrects[i].collidelist(enemies)
            if collision != -1:
                to_delete.append(i)
                
        for x in to_delete:
            del self.bulletrects[x]
                
