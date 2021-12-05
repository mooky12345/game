import pygame
from pygame import surface
from main import background
class Auto_cannon(pygame.sprite.Sprite):
    def __init__(self,radium):
        super().__init__()
        self.image = pygame.Surface([radium*2,radium*2])
        self.rect.center = (750,0)
        self.image.fill((0,0,0,0))
        pygame.draw.circle(self.image, (255,255,0,100), (radium,radium), radium)
        self.blit_base()
    def blit_base(self):
        background.blit(self.image,self.rect)
    def shooting(self):
        pass
    def rotating(self):
        pass