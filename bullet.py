# -*- coding: iso-8859-1 -*-
import sys, pygame

class Bullet:
    is_firing = False
    bullet = pygame.image.load("res/bullet.png").convert()
    bulletrect = bullet.get_rect()
    bullet_speed = [0, -3]
    bulletrects = []
    #bullets = []

    def fire(self, pshiprect):
        #self.bullets.append(self.bullet)
        self.bulletrects.append(self.bulletrect)
        
        self.bulletrect = self.bullet.get_rect()
        self.bulletrect.move_ip(pshiprect)
        self.is_firing = True
                
    def move(self, screen):       
        #if self.is_firing:
        for i in range(len(self.bulletrects)):
            self.bulletrects[i] = self.bulletrects[i].move(self.bullet_speed)
            screen.blit(self.bullet, self.bulletrects[i])
            
            #If bullet goes off the top of the screen
            if self.bulletrect.top < 0:
                self.is_firing = False
    