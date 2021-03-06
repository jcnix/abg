# -*- coding: utf-8 -*-

import sys, pygame, properties, time

class Menu:
    screen = None
    banner = pygame.image.load("res/abgbanner.png").convert()
    bannerrect = banner.get_rect()
    blackSurface = pygame.Surface([banner.get_width(), banner.get_height()])
    blackSurface.fill([0,0,0])
    
    def __init__(self, screen):
        self.screen = screen
    
    def showMenu(self):
        inMenu = True
        self.screen.blit(self.banner, self.bannerrect)     
        pygame.display.update(self.bannerrect)
        while inMenu:
            time.sleep(.1)
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.screen.blit(self.blackSurface, self.bannerrect)     
                        pygame.display.update(self.bannerrect)                 
                        inMenu = False
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
