import pygame
from pygame.sprite import spritecollide
class ouohand(pygame.sprite.Sprite):
    def __init__(self):
        self.surf = pygame.Surface([30,120])
        self.rect = self.surf.get_rect()
        self.rect.center = (-100,-100)
        self.direction = None
        self.exist = False
        self.spped = 10
        self.cooldown = 100
    def implement(self,pos):
        self.exist = True
        self.cooldown = 100
        if self.cooldown == 0:
            if self.direction  == 0:
                self.rect.bottomleft = (pos[0]+30,pos[1])
            if self.direction  == 180:
                self.rect.bottomright = (pos[0],pos[1])
    def update(self,dir):
        self.cooldown_creasing()
        self.direction = dir
        if self.exist:
            if self.direction == 0:
                self.rect.left += self.speed
            if self.direction  == 180:
                self.rect.right -= self.speed
            if self.rect.left > 1500 or self.rect.right < 0:
                self.exist = False
                self.rect.center = (-100,-100)
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1