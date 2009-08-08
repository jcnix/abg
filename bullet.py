# -*- coding: iso-8859-1 -*-

# File:   bullet.py
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
from enemy import Enemy

class Bullet:
    bullet = pygame.image.load("res/bullet.png").convert()
    bulletrect = bullet.get_rect()
    bulletrects = []
    blackSurface = pygame.Surface([bullet.get_height(), bullet.get_width()])
    blackSurface.fill([0,0,0])
    screen = None

    def set_screen(self, screen):
        self.screen = screen

    def fire(self, pshiprect):       
        self.bulletrect = self.bullet.get_rect()
        self.bulletrect.move_ip(pshiprect)
        self.bulletrects.append(self.bulletrect)
                
    def move(self, enemy):
        to_update = []
        if len(self.bulletrects) > 0:
            bullet_speed = [0, -600]
            bullet_speed = frametime.modify_speed(bullet_speed)
            enemies = enemy.getEnemies()
            to_delete = []
            to_update += self.bulletrects
            
            for i in range(len(self.bulletrects)):
                self.screen.blit(self.blackSurface, self.bulletrects[i])
                self.bulletrects[i] = self.bulletrects[i].move(bullet_speed)
                self.screen.blit(self.bullet, self.bulletrects[i])
                
                #If bullet goes off the top of the screen
                if self.bulletrects[i].top < 0:
                    to_delete.append(i)
                
                #If bullet hits an enemy
                collision = self.bulletrects[i].collidelist(enemies)
                if collision != -1:
                    to_delete.append(i)
                    enemy.remove(collision)
            
            for x in to_delete:
                self.remove(x)
            
        to_update += self.bulletrects
                
        return to_update
    
    def remove(self, index):
        try:
            self.screen.blit(self.blackSurface, self.bulletrects[index])
            del self.bulletrects[index]
        except IndexError:
            print "IndexError for bullet %d", index
