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

#class to handle all enemies on screen

import sys, pygame, frametime, properties, random
from enemy import Enemy

class Enemies:
    enemies = []
    blackSurface = pygame.Surface([Enemy.enemy.get_width(), Enemy.enemy.get_height()])
    blackSurface.fill([0,0,0])
    screen = None
    
    def set_screen(self, screen):
        self.screen = screen
    
    def create(self):
        #range that the current player ship can shoot
        where_spawn = random.randint(1, properties.width - Enemy.enemy.get_width())
        
        lenemy = Enemy(where_spawn)
        self.enemies.append(lenemy)

    def move(self, bullet):
        to_update = []
        if frametime.can_create_enemy():
            self.create()
        
        to_delete = []
        to_update += [x.enemyrect for x in self.enemies]
        
        if len(self.enemies) > 0:
            for i in range(len(self.enemies)):
                self.enemies[i].update(bullet)
                self.screen.blit(self.blackSurface, self.enemies[i].enemyrect)
                self.screen.blit(Enemy.enemy, self.enemies[i].enemyrect)
                
                #If enemy goes off the bottom of the screen
                if self.enemies[i].enemyrect.top > 800:
                    to_delete.append(i)
                    
            for x in to_delete:
                self.remove(x)
            
        to_update += [x.enemyrect for x in self.enemies]
        return to_update
        
    def getEnemies(self):
        return self.enemies
        
    def remove(self, index):
        try:
            to_update = self.enemies[index].enemyrect
            self.screen.blit(self.blackSurface, self.enemies[index].enemyrect)
            del self.enemies[index]
            return to_update
        except IndexError:
            print("IndexError for enemy {0} of {1}".format(index, len(self.enemies)))
            
    def game_over(self):
        for i in range(len(self.enemies)):
            self.screen.blit(self.blackSurface, self.enemies[i].enemyrect)
            
        del self.enemies[:]
            