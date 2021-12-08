import pygame
class ouofoot(pygame.sprite.Sprite):
    def __init__(self):
        self.surf = pygame.Surface([120,30])
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
                self.rect.topleft = (pos[0]+30,pos[1])
            if self.direction  == 180:
                self.rect.topright = (pos[0],pos[1])
    def update(self,pos,dir):
        self.cooldown_creasing()
        self.direction = dir
        if self.exist:
            if self.direction  == 0:
                pass
            if self.direction  == 180:
                pass
            if self.rect.top > pos[1] + 60:
                self.rect.center = (-100,-100)
                self.exist = False
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1
