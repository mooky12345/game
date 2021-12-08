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
    def implement(self,pos,dir):
        self.exist = True
        self.direction = dir
        self.cooldown = 100
        if self.cooldown == 0:
            if dir == 0:
                self.rect.topleft = (pos[0]+30,pos[1])
            if dir == 180:
                self.rect.topright = (pos[0],pos[1])
    def update(self,pos):
        self.cooldown_creasing()
        if self.exist:
            if self.dir == 0:
                pass
            if self.dir == 180:
                pass
            if self.rect.top > pos[1] + 60:
                self.rect.center = (-100,-100)
                self.exist = False
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1
