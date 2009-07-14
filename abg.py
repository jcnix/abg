# -*- coding: iso-8859-1 -*-
import sys, pygame
pygame.init()

size = width, height = 800, 600
move_right = [1, 0]
move_left = [-1, 0]
bullet_speed = [0, -3]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Alpha Beta Gamma")
pygame.key.set_repeat(1, 1)

pship = pygame.image.load("res/player_ship.png").convert()
pshiprect = pship.get_rect()

pshiprect.move_ip(width/2, height - 25)

bullet = pygame.image.load("res/bullet.png").convert()
bulletrect = bullet.get_rect()

bulletrect.move_ip(width/2, height - 25)
is_firing = False

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and pshiprect.right < width:
                pshiprect = pshiprect.move(move_right)
            if event.key == pygame.K_LEFT and pshiprect.left > 0:
                pshiprect = pshiprect.move(move_left)
            if event.key == pygame.K_SPACE:
                is_firing = True
    
    screen.fill(black)
    
    if is_firing:
        bulletrect = bulletrect.move(bullet_speed)
        screen.blit(bullet, bulletrect)
        #If bullet goes off the top of the screen
        if bulletrect.top < 0:
            is_firing = False
    
    screen.blit(pship, pshiprect)
    
    pygame.display.flip()
