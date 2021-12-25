import pygame
import math
class ouofoot(pygame.sprite.Sprite):
    def __init__(self):
        self.surf = pygame.Surface([120,30]).convert()
        self.rect = self.surf.get_rect()
        self.rect.center = (-100,-100)
        self.surf.fill((0,0,0,100))
        self.direction = None
        self.exist = False
        self.spped = 10
        self.lenth = None
        self.angle = 1000
        self.cooldown = 100
        self.max_cooldown = 100
        self.center = None
        self.angle1 = 1000
        self.lenth1 = None
        self.surf_lenth = 120
    def implement(self,pos,dir,rect):
        
        self.direction = dir
       
        if self.cooldown == 0:
            self.exist = True
            self.cooldown = 100
            if self.direction  == 0:
                self.rect.topleft = (pos[0]+30,pos[1])
            if self.direction  == 180:
                self.rect.topright = (pos[0],pos[1])
            self.get_varible()
    def get_varible(self):
        self.lenth = math.hypot(self.rect.top - self.center[1],self.rect.left - self.center[0])+2
        self.lenth1 = math.hypot(self.rect.top - self.center[1],self.rect.right - self.center[0])+2
        self.angle = math.degrees(math.atan2(self.rect.top - self.center[1],self.rect.left - self.center[0]))
        self.angle1 = math.degrees(math.atan2(self.rect.top - self.center[1],self.rect.right - self.center[0]))
    def update(self,rect,players):

        self.cooldown_creasing()
        self.center = rect.center
        self.angle1 += 5
        self.angle -= 5
        if self.exist:
            self.get_varible()
            if pygame.sprite.spritecollide(self,players,False):
                hits = pygame.sprite.spritecollide(self,players,False)
                self.explosion_cooldown = 300
                for player in hits:
                    player.blood.cut_blood(20,True)
                    player.knock_back(self.rect.center,10,40)
            if self.rect.top < rect.top+13:
                self.rect.top -= 1
            else:
                if self.direction  == 0:
                    self.rect.top = self.center[1]+self.lenth*math.sin(math.radians(self.angle)) 
                    self.rect.left = self.center[0]+self.lenth*math.cos(math.radians(self.angle)) 
                    print(self.rect.topleft)
                if self.direction == 180:
                    self.rect.top = self.center[1]+self.lenth1*math.sin(math.radians(self.angle1)) 
                    self.rect.right = self.center[0]+self.lenth1*math.cos(math.radians(self.angle1)) 
                    print(self.rect.topright)
            if self.rect.top < rect.top-30:
                self.rect.center = (-100,-100)
                self.exist = False
            
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1
