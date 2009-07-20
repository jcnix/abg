# -*- coding: iso-8859-1 -*-
import sys, pygame

class Bullet:
    screen = None
    is_firing = False
    
    def __init__(self, tscreen):
        global screen
        screen = tscreen
    
    def fire(self):
        bullet_speed = [0, -3]
        bullet = pygame.image.load("res/bullet.png").convert()

        #bulletrect.move_ip(pshiprect.midtop)
        bulletrect = bullet.get_rect()
        
        global is_firing
        is_firing = True
        if is_firing:
            bulletrect = bulletrect.move(bullet_speed)
            
            global screen
            screen.blit(bullet, bulletrect)
            #If bullet goes off the top of the screen
            if bulletrect.top < 0:
                is_firing = False
                #bulletrect.move_ip(pshiprect.midtop)
    