# -*- coding: iso-8859-1 -*-
import sys, pygame

class Bullet:
    
    def fire(self, pshiprect, screen):
        is_firing = False
        bullet = pygame.image.load("res/bullet.png").convert()
        bulletrect = bullet.get_rect()
        
        bullet_speed = [0, -3]
        
        bulletrect.move_ip(pshiprect.midtop)
        
        is_firing = True
        while is_firing:
            bulletrect = bulletrect.move(bullet_speed)
            
            screen.blit(bullet, bulletrect)
            pygame.display.flip()
            #If bullet goes off the top of the screen
            if bulletrect.top < 0:
                is_firing = False
    