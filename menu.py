# -*- coding: utf-8 -*-

import pygame

class Menu:
    screen = None
    
    def __init__(self, screen):
        self.screen = screen
    
    def showMenu(self):
        inMenu = True
        while inMenu:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        inMenu = False
