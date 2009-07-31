# -*- coding: utf-8 -*-
from time import time

start_time = 0
end_time = 0
diff_time = 0

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
    