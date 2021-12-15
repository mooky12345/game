import pygame
from character3.explosion import explosion
import math
class missile():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface([60,60]).convert()
        self.surf.fill((0,0,0,100))
        self.rect = self.surf.get_rect()
        self.rect.center = (-100,-100)
        self.cooldown = 300
        self.explosion_cooldown = 1000
        self.direction = 180
        self.exist = False 
        self.speed = 1
        self.pos = [-100,-100]
        self.explosion = explosion()
    def implement(self,pos,dir):
        self.direction = dir
        print(self.cooldown)
        if self.cooldown == 0:
            self.exist = True
            self.cooldown = 300
            if self.direction == 0:
                #self.rect.bottomleft = (pos[0]+31,pos[1])
                self.pos[0] = 0
                self.pos[1] = 100
            if self.direction == 180:
                #self.rect.bottomright = (pos[0]-1,pos[1])
                self.pos[0] = 0
                self.pos[1] = 100
    def out_width(self):
        self.rect.center = (-100,-100)
        self.pos[0] = -100
        self.pos[1] = -100
    def reset_cooldown(self):
        self.cooldown = 300
    def update(self,player):
        if self.exist:
            angle = (180-math.degrees(math.atan2((player.pos[1]-self.rect.center[1]),(player.pos[0]-self.rect.center[0]))))
            self.pos[0] -= self.speed*math.cos(math.radians(angle))
            self.pos[1] += self.speed*math.sin(math.radians(angle))
            if self.rect.colliderect(player.rect) == 1:
                self.exist = False
                self.explosion.implement(self.rect.bottomleft,self.direction)
                self.out_width()
            if  self.explosion_cooldown == 100:
                pass
            if  self.explosion_cooldown == 0:
                self.exist = False
                self.explosion.implement(self.rect.bottomleft,self.direction)
                self.explosion_cooldown = 300
                self.out_width()
            self.explosion_cooldown_creasing()
            self.rect.bottomleft = self.pos
        self.explosion.update(player)
        self.cooldown_creasing()
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1
    def explosion_cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1      
    def knock_back(player,dir):
        pass