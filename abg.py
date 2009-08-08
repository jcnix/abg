#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#
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

screen = pygame.display.set_mode(size)

from bullet import Bullet
from enemy import Enemy
bullet = Bullet()
bullet.set_screen(screen)
enemy = Enemy()
enemy.set_screen(screen)

pygame.display.set_caption("Alpha Beta Gamma")
pygame.key.set_repeat()

pship = pygame.image.load("res/player_ship.png").convert()
pshiprect = pship.get_rect()

blackSurface = pygame.Surface([pship.get_height(), pship.get_width()])
blackSurface.fill([0,0,0])

pshiprect.move_ip(width/2, height - 25)
enemy.create()

while 1:
    frametime.start()
    to_update = []
    move_right = [325, 0]
    move_left = [-325, 0]
    move_right = frametime.modify_speed(move_right)
    move_left = frametime.modify_speed(move_left)
    
    pygame.event.pump()
    key = pygame.key.get_pressed()
    
    if key[pygame.K_ESCAPE]:
        sys.exit()

    to_update.append(pshiprect)
    screen.blit(blackSurface, pshiprect)
    if key[pygame.K_RIGHT] and pshiprect.right < width:
        pshiprect = pshiprect.move(move_right)
        
    if key[pygame.K_LEFT] and pshiprect.left > 0:
        pshiprect = pshiprect.move(move_left)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet.fire(pshiprect.midtop)
    
    screen.blit(pship, pshiprect)
    to_update.append(pshiprect)
    to_update += bullet.move(enemy)
    to_update += enemy.move()
    pygame.display.update(to_update)

    #find how long it took to render this frame so we can adjust speeds
    frametime.end()
    