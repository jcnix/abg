# -*- coding: utf-8 -*-

# finds the amount of time it took to render a frame
# and converts pixels/sec to pixels/frame so that
# objects can move at the desired speed no matter
# what the fps is

# This module can also measure the time and figure
# out if a new enemy can be spawned.

from time import time

start_time = 1
end_time = 0
diff_time = 1
spawn_time = 0

def start():
    global start_time
    start_time = time()
    
    return start_time
    
def end():
    global start_time
    global end_time
    global diff_time
    
    end_time = time()
    diff_time = end_time - start_time
    start_time = end_time

    return diff_time
    
def get_diff_time():
    return diff_time
    
def modify_speed(lspeed):
    return [diff_time*x for x in lspeed]
    
def can_create_enemy():
    global spawn_time
    spawn_time += diff_time
    
    #spawn time is 5 seconds, just a placeholder for now
    if spawn_time >= 3:
        spawn_time = 0
        return True
    else:
        return False
