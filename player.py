# -*- coding: iso-8859-1 -*-

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

import sys, pygame, frametime, properties

class Player:
    pship = pygame.image.load("res/player_ship.png").convert()
    pshiprect = pship.get_rect()
    
    blackSurface = pygame.Surface([pship.get_width(), pship.get_height()])
    blackSurface.fill([0,0,0])
    
    screen = None
    time_to_cooldown = 0.25
    cooldown_time = 0.25

    def set_screen(self, screen):
        self.screen = screen
        self.pshiprect.move_ip(properties.size[0]/2, properties.size[1] - 25)
        self.screen.blit(self.pship, self.pshiprect)
        
        self.width = properties.size[0]
        self.height = properties.size[1]
        return [self.pshiprect]
    
    def move_left(self):
        to_update = []
        to_update += [self.pshiprect]
        
        if self.pshiprect.left > 0:
            move_left = [-325, 0]
            move_left = frametime.modify_speed(move_left)
            
            self.screen.blit(self.blackSurface, self.pshiprect)
            self.pshiprect = self.pshiprect.move(move_left)
            self.screen.blit(self.pship, self.pshiprect)
            
        to_update += [self.pshiprect]
        return to_update
        
    def move_right(self):
        to_update = []
        to_update += [self.pshiprect]
        
        if self.pshiprect.right < self.width:
            move_right = [325, 0]
            move_right = frametime.modify_speed(move_right)
            
            self.screen.blit(self.blackSurface, self.pshiprect)
            self.pshiprect = self.pshiprect.move(move_right)
            self.screen.blit(self.pship, self.pshiprect)
            
        to_update += [self.pshiprect]
        return to_update
        
    def fire(self, bullet):
        diff_time = frametime.get_diff_time()
        self.cooldown_time += diff_time
        
        if self.cooldown_time > self.time_to_cooldown:
            self.cooldown_time = 0
            bullet.player_fire(self.pshiprect.midtop)
