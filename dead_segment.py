import pygame
from pygame import sprite
import random 
vec = pygame.math.Vector2
class dead_segment(pygame.sprite.Sprite):
    def __init__(self,pos,dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,10]).convert()
        self.image.fill((255,0,0,100))
        self.rect = self.image.get_rect()
        self.rect.center = (-100,-100)
        self.cooldown = 200
        self.direction = dir
        self.vel = [random.uniform(3,10),random.uniform(3,10)]     
        self.init_pos(pos)
    def init_pos(self,pos):
        pos[1] -= 20
        self.rect.center = pos
        pos[1] += 20
    def update(self,platforms):
        if self.cooldown == 0:
            self.kill()
        if self.direction == 0:
            self.rect.x += self.vel[0] 
        if self.direction == 180:
            self.rect.x -= self.vel[0] 
        if pygame.sprite.spritecollide(self,platforms,False):
            self.vel[1] = 0
            self.vel[0] = 0
        self.rect.y -= self.vel[1]
        self.vel[1] -= 0.5
        self.cooldown_creasing()
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1