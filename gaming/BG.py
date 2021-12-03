import pygame
from genericpath import isfile
from pathlib import Path
import os
from pygame.locals import *

WIDTH = 1500
HEIGHT=800

class background_test(pygame.sprite.Sprite):
    def __init__(self,image="background/1.jpg"):
        super().__init__()
        self.bg_x = 225
        self.bg_y = 0
        self.bg = pygame.image.load(image)
        self.bg = pygame.transform.scale(self.bg, (1500, 800))
        self.surf = pygame.Surface((1500, 800))
        self.rect = self.surf.get_rect()
        self.surf.blit(self.bg, (0, 0))
        self.test=0
        self.test_y =0
    def redraw(self, change_x,change_y):
        self.bg_x = change_x
        self.bg_y=change_y
        self.pos_x=change_x
        self.pos_y=change_y
        if change_x>WIDTH/2 and change_x<900-WIDTH/2:
             self.pos_x=WIDTH/2
        elif change_x>900-WIDTH/2:
             self.pos_x=WIDTH-(900-self.pos_x)

        self.hitbox = (self.pos_x, self.pos_y - 60, 28, 60)

        if self.bg_x < WIDTH / 2:
            self.test=0
        elif self.bg_x > WIDTH / 2 and self.bg_x < 900 - WIDTH / 2:
            self.test=-(self.bg_x - WIDTH/2)
        elif self.bg_x > 900 - WIDTH / 2:
            self.test=-(900 - WIDTH)


        if self.bg_y<100:
             self.test_y=100-self.bg_y
        if self.bg_y>=100:self.test_y=0
        # if change_x:
            # if self.bg_x < WIDTH/2:
            #     self.surf.blit(self.bg, (0, self.bg_y))
            # elif self.bg_x > WIDTH/2 and self.bg_x < 900 - WIDTH/2:
            #     self.surf.blit(self.bg, (-(self.bg_x - WIDTH/2), self.bg_y))
            # elif self.bg_x > 900 - WIDTH/2:
            #     self.surf.blit(self.bg, (-(900 - WIDTH), self.bg_y))

        self.surf.blit(self.bg, (self.test, self.test_y))
        pygame.draw.rect(self.surf,[255,0,0],self.hitbox,0)
        # if change_y:
        #     if self.pos_y>400:
        #         self.surf

        

        
