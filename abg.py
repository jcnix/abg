# -*- coding: iso-8859-1 -*-

# File:   abg.py
# Author: Casey Jones
#
# Created on July 20, 2009, 4:48 PM
#
# This file is part of Alpha Beta Gamma (abg).
#
# ABG is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ABG is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ABG.  If not, see <http://www.gnu.org/licenses/>.

import sys, pygame, frametime

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
frametime.start()
enemy.create()

while 1:
    move_right = [375, 0]
    move_left = [-375, 0]
    move_right = frametime.modify_speed(move_right)
    move_left = frametime.modify_speed(move_left)
    
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
    bullet.move(screen, enemy)
    enemy.move(screen)
    
    pygame.display.flip()

    #find how long it took to render so we can adjust speeds
    frametime.end()
    
