import pygame
import math
WHITE = (0,0,0)
class Shield():
    def __init__(self,width,height):
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

    
        self.width = width
        self.height = height
        pygame.draw.circle(self.image, self.color, (self.width//2, self.height//2), 5)
        self.rect = self.image.get_rect()