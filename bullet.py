# -*- coding: iso-8859-1 -*-
import sys, pygame

class Bullet:
    bullet = pygame.image.load("res/bullet.png").convert()
    bulletrect = bullet.get_rect()
    bullet_speed = [0, -3]
    bulletrects = []

    def fire(self, pshiprect):       
        self.bulletrect = self.bullet.get_rect()
        self.bulletrect.move_ip(pshiprect)
        self.bulletrects.append(self.bulletrect)
                
    def move(self, screen):
        to_delete = []
        
        for i in range(len(self.bulletrects)):
            self.bulletrects[i] = self.bulletrects[i].move(self.bullet_speed)
            screen.blit(self.bullet, self.bulletrects[i])
            
            #If bullet goes off the top of the screen
            if self.bulletrects[i].top < 0:
                to_delete.append(self.bulletrects[i])
        
        for x in range(len(to_delete)):
            del self.bulletrects[x]
                