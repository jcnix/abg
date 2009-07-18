# -*- coding: iso-8859-1 -*-
import sys, pygame

class Bullet:
    bullet_speed = [0, -3]
    bullet = pygame.image.load("res/bullet.png").convert()
    bulletrect = bullet.get_rect()

    #bulletrect.move_ip(pshiprect.midtop)
    is_firing = False
    
    def fire(self):
        is_firing = True
        if is_firing:
            bulletrect = bulletrect.move(bullet_speed)
            screen.blit(bullet, bulletrect)
            #If bullet goes off the top of the screen
            if bulletrect.top < 0:
                is_firing = False
                bulletrect.move_ip(pshiprect.midtop)
    