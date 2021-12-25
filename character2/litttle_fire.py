import pygame
from pygame import sprite
import random 
class little_fireball(pygame.sprite.Sprite):
    def __init__(self,pos,dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10,10]).convert()
        self.image.fill((0,255,0,100))
        self.rect = self.image.get_rect()
        self.rect.center = (-100,-100)
        self.cooldown = 200
        self.direction = dir
        self.vel = [random.uniform(3,10),random.uniform(3,10)]     
        self.init_pos(pos)
    def init_pos(self,pos):
        self.rect.center = pos
    def update(self,players,platforms):
        if pygame.sprite.spritecollide(self,players,False):
            hits=pygame.sprite.spritecollide(self,players,False)
            for player in hits:
                player.blood.cut_blood(0.1,True)
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