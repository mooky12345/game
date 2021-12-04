import pygame
import math
BLACK = (0,0,0)

class Shield(pygame.sprite.Sprite):
    def __init__(self,radium,color,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([radium*2, radium*2]) 
        self.image.fill(BLACK) 
        pygame.draw.circle(self.image, color, (radium,radium), radium)
        self.rect = self.image.get_rect()  
        self.rect.center = (x,y)  