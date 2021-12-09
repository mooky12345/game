import pygame
from pygame.sprite import spritecollide
class transport_damage(pygame.sprite.Sprite):
    def __init__(self):
        self.surf1 = pygame.Surface([30,120]).convert()
        self.surf1.fill((0,0,0,100))
        self.rect1 = self.surf.get_rect()
        self.rect1.center = (-100,-100)
        self.surf2 = pygame.Surface([30,120]).convert()
        self.surf2.fill((0,0,0,100))
        self.rect2 = self.surf.get_rect()
        self.rect2.center = (-100,-100)
        self.exist = False
        self.speed = 10
        self.cooldown = 100
            
    def implement(self,pos,dir):
        self.exist = True
        self.direction = dir
        if self.cooldown == 0:
            self.cooldown = 100 
            if self.direction  == 0:
                self.rect.bottomleft = (pos[0]+30,pos[1])
            if self.direction  == 180:
                self.rect.bottomright = (pos[0],pos[1])
    def transport(self):
        pass
    def update(self):
        self.cooldown_creasing()
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
