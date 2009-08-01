# -*- coding: utf-8 -*-

#finds the amount of time it took to render a frame
#and converts pixels/sec to pixels/frame so that
#objects can move at the desired speed no matter
#what the fps is

from time import time

start_time = 1
end_time = 0
diff_time = 1

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
    
