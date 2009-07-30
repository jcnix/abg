# -*- coding: iso-8859-1 -*-
import sys, pygame
from time import time

pygame.init()

size = width, height = 800, 600
black = 0, 0, 0

screen = pygame.display.set_mode(size)

from bullet import Bullet
from enemy import Enemy
bullet = Bullet()
enemy = Enemy();

pygame.display.set_caption("Alpha Beta Gamma")
pygame.key.set_repeat()

pship = pygame.image.load("res/player_ship.png").convert()
pshiprect = pship.get_rect()

pshiprect.move_ip(width/2, height - 25)
current_time = time()
end_time = current_time

while 1:
    move_right = [1.5, 0]
    move_left = [-1.5, 0]
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
    enemy.init(screen)
    enemies = enemy.getEnemies()
    bullet.move(screen, enemies)
    
    pygame.display.flip()

    #find how long it took to render so we can adjust speeds
    end_time = time()
    diff_time = end_time - current_time
    current_time = end_time
    
    move_right = [diff_time*x for x in move_right]
    move_left = [diff_time*x for x in move_left]