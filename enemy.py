# -*- coding: utf-8 -*-

# File:   enemy.py
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
import random

class Enemy:
    enemy = pygame.image.load("res/enemy.png").convert()
    enemyrect = enemy.get_rect()
    enemies = []
    
    def create(self):
        #range that the current player ship can shoot
        where_spawn = random.randint(1, 800-50)
        
        self.enemyrect = self.enemy.get_rect()
        self.enemies.append(self.enemyrect)
        self.enemyrect.move_ip(where_spawn, 0)

    def move(self, screen):
        if frametime.can_create_enemy():
            self.create()
            
        move_speed = [0, 250]
        move_speed = frametime.modify_speed(move_speed)
        to_delete = []
        
        if len(self.enemies) > 0:
            for i in range(len(self.enemies)):
                self.enemies[i] = self.enemies[i].move(move_speed)
                screen.blit(self.enemy, self.enemies[i])
                
                #If enemy goes off the bottom of the screen
                if self.enemies[i].top > 800:
                    to_delete.append(i)
                    
            for x in to_delete:
                self.remove(x)
            
            print len(self.enemies)
        
    def getEnemies(self):
        return self.enemies
        
    def remove(self, index):
        try:
            del self.enemies[index]
        except IndexError:
            print "IndexError for enemy %d", index