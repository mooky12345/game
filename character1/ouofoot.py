import pygame
import math
class ouofoot(pygame.sprite.Sprite):
    def __init__(self):
        self.surf = pygame.Surface([120,30])
        self.rect = self.surf.get_rect()
        self.rect.center = (-100,-100)
        self.direction = None
        self.exist = False
        self.spped = 10
        self.cooldown = 100
    def implement(self,pos,dir):
        self.exist = True
        self.direction = dir
       
        if self.cooldown == 0:
            self.cooldown = 100
            if self.direction  == 0:
                self.rect.topleft = (pos[0]+30,pos[1])
            if self.direction  == 180:
                self.rect.topright = (pos[0],pos[1])
    def update(self,rect):
        self.cooldown_creasing()
        center = rect.center
        
        lenth = math.hypot(self.rect.top - center[1],self.rect.left - center[0])
        degree = math.degrees(math.atan2(self.rect.top - center[1],self.rect.left - center[0]))
       
        degree += 1
        if self.exist:
            print(lenth)
            if self.direction  == 0:
                self.rect.top = lenth*math.degrees(math.sin(degree))
                self.rect.left = lenth*math.degrees(math.cos(degree))
            if self.direction  == 180:
                pass
            if self.rect.top > rect.top + 5:
                self.rect.center = (-100,-100)
                self.exist = False
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1
