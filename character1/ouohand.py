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
    def implement(self,pos,dir):
        self.exist = True
        self.direction = dir
        self.cooldown = 100
        if self.cooldown == 0:
            if dir == 0:
                self.rect.topleft = (pos[0],pos[1])
            if dir == 180:
                self.rect.topright = (pos[0],pos[1])
    def update(self):
        self.cooldown_creasing()
        if self.exist:
            if dir == 0:
                self.rect.bottomleft += self.speed
            if dir == 180:
                self.rect.right -= self.speed
            if self.rect.bottomleft > 1500 or self.rect.bottomright < 0:
                self.exist = False
                self.rect.center = (-100,-100)
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1
