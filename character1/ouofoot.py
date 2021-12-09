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
        
        self.direction = dir
       
        if self.cooldown == 0:
            self.exist = True
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
        
        degree += 0.1
        if self.exist:
            print(self.rect.topleft)
            print(degree)
            if self.direction  == 0:
                
                self.rect.top = rect.center[1]+lenth*math.sin(math.degrees(degree))
                self.rect.left = rect.center[0]+lenth*math.cos(math.degrees(degree))
                print(lenth*math.sin(math.degrees(degree)))
                print(self.rect.topleft)
            if self.direction  == 180:
                pass
            if self.rect.top > rect.top + 100:
                self.rect.center = (-100,-100)
                self.exist = False
            print(self.rect.topleft)
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1
