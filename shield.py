import pygame
import math
BLACK = (0,0,0)

class Shield(pygame.sprite.Sprite):
    def __init__(self,radium,vision,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([radium*2, radium*2]).convert_alpha()
        self.radium = radium
        self.image.fill((0,0,0,0))
        pygame.draw.circle(self.image, (255,255,0,0), (radium,radium), radium)
        self.rect = self.image.get_rect()  
        self.rect.center = (x,y)  
    def change_visible(self):
        pygame.draw.circle(self.image, (255,255,0,100), (self.radium,self.radium), self.radium)
    def change_invisible(self):
        pygame.draw.circle(self.image, (255,255,0,0), (self.radium,self.radium), self.radium)