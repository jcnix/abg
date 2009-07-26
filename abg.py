# -*- coding: iso-8859-1 -*-
import sys, pygame
pygame.init()

size = width, height = 800, 600
move_right = [1, 0]
move_left = [-1, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

from bullet import Bullet
bullet = Bullet()

pygame.display.set_caption("Alpha Beta Gamma")
pygame.key.set_repeat()

pship = pygame.image.load("res/player_ship.png").convert()
pshiprect = pship.get_rect()

pshiprect.move_ip(width/2, height - 25)

while 1:
    pygame.event.pump()
    key = pygame.key.get_pressed()
    
    if key[pygame.K_ESCAPE]: 
        sys.exit()

    if key[pygame.K_RIGHT] and pshiprect.right < width:
        pshiprect = pshiprect.move(move_right)
    if key[pygame.K_LEFT] and pshiprect.left > 0:
        pshiprect = pshiprect.move(move_left)
        
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet.fire(pshiprect.midtop)
    
    screen.fill(black)
    
    screen.blit(pship, pshiprect)
    bullet.move(screen)
    
    pygame.display.flip()
