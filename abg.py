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

import sys, pygame, frametime, properties, time

pygame.init()

screen = pygame.display.set_mode(properties.size)

from player import Player
from bullet import Bullet
from enemies import Enemies

player = Player()
to_update = player.set_screen(screen)
#draw player to screen immediately
pygame.display.update(to_update)

bullet = Bullet()
bullet.set_screen(screen)

enemies = Enemies()
enemies.set_screen(screen)

pygame.display.set_caption("Alpha Beta Gamma")
pygame.key.set_repeat()

while 1:
    to_update = []
    
    pygame.event.pump()
    key = pygame.key.get_pressed()
    
    if key[pygame.K_ESCAPE]:
        sys.exit()

    if key[pygame.K_RIGHT]:
        to_update += player.move_right()
    if key[pygame.K_LEFT]:
        to_update += player.move_left()
    if key[pygame.K_SPACE]:
        player.fire(bullet)
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                isPaused = True
                while isPaused:
                    time.sleep(1)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                isPaused = False
                       
    frametime.start()
    to_update += bullet.move(enemies)
    to_update += enemies.move(bullet)
    pygame.display.update(to_update)
    
    #find how long it took to render this frame so we can adjust speeds
    frametime.end()
    