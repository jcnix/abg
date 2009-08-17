# -*- coding: utf-8 -*-

# File:   frametime.py
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

######
# finds the amount of time it took to render a frame
# and converts pixels/sec to pixels/frame so that
# objects can move at the desired speed no matter
# what the fps is

# This module can also measure the time and figure
# out if a new enemy can be spawned.

import time
#from time import time

start_time = 1
end_time = 0
diff_time = 1
spawn_time = 0

def start():
    global start_time
    start_time = time.time()
    
    return start_time
    
def end():
    global start_time
    global end_time
    global diff_time
    
    end_time = time.time()
    diff_time = end_time - start_time
    if diff_time < 0.010:
        time.sleep(0.010 - diff_time)
        diff_time = 0.010

    return diff_time
    
def get_diff_time():
    return diff_time
    
def modify_speed(lspeed):
    return [diff_time*x for x in lspeed]
    
def can_create_enemy():
    global spawn_time
    spawn_time += diff_time
    
    #spawn time is 5 seconds, just a placeholder for now
    if spawn_time >= 0.75:
        spawn_time = 0
        return True
    else:
        return False
