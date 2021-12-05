import pygame
from pygame import surface
from main import background
class Auto_cannon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([100,100])
        self.rect.center = (750,0)
        self.blit_base()
    def blit_base(self):
        background.blit(self.image,self.rect)
    def shooting(self):
        pass
    def rotating(self):
        pass