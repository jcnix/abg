# -*- coding: iso-8859-1 -*-
import sys, pygame, enemy

class Bullet:
    bullet = pygame.image.load("res/bullet.png").convert()
    bulletrect = bullet.get_rect()
    bulletrects = []

    def fire(self, pshiprect):       
        self.bulletrect = self.bullet.get_rect()
        self.bulletrect.move_ip(pshiprect)
        self.bulletrects.append(self.bulletrect)
                
    def move(self, screen, diff_time, enemies):
        bullet_speed = [0, -3]
        bullet_speed = [(diff_time+1)*x for x in bullet_speed]
        
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
                