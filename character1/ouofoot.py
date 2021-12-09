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
        self.lenth = None
        self.angle = 1000
        self.cooldown = 100
        self.center = None
        self.angle1 = 1000
        self.lenth1 = None
    def implement(self,pos,dir,rect):
        
        self.direction = dir
       
        if self.cooldown == 0:
            self.exist = True
            self.cooldown = 100
            if self.direction  == 0:
                self.rect.topleft = (pos[0]+30,pos[1])
            if self.direction  == 180:
                self.rect.topright = (pos[0],pos[1])
            self.get_varible(rect)
    def get_varible(self,rect):
        self.center = rect.center
        self.lenth = math.hypot(self.rect.top - self.center[1],self.rect.left - self.center[0])+2
        self.lenth1 = math.hypot(self.rect.top - self.center[1],self.rect.right - self.center[0])+2
        self.angle1 = math.degrees(math.atan2(self.rect.top - self.center[1],self.rect.right - self.center[0]))
        self.angle = math.degrees(math.atan2(self.rect.top - self.center[1],self.rect.left - self.center[0]))
    def update(self,rect):
        self.cooldown_creasing()
        
        self.angle1 += 3
        self.angle -= 3
        if self.exist:
            if self.direction  == 0:
                self.rect.top = self.center[1]+self.lenth*math.sin(math.radians(self.angle)) 
                self.rect.left = self.center[0]+self.lenth*math.cos(math.radians(self.angle)) 
            if self.direction == 180:
                self.rect.top = self.center[1]+self.lenth1*math.sin(math.radians(self.angle1)) 
                self.rect.right = self.center[0]+self.lenth1*math.cos(math.radians(self.angle1)) 
            if self.rect.top < rect.top:
                pass
                self.rect.center = (-100,-100)
                self.exist = False
            print(self.rect.top)
            print(rect.top)
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1
