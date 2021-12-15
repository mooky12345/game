import pygame

class explosion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = 1
        self.surf = pygame.Surface([self.size,self.size]).convert()
        self.surf.fill((0,255,0,100))
        self.rect = self.surf.get_rect()
        self.rect.center = (-100,-100)
        self.cooldown = 100
        self.direction = None
        self.exist = False 
    def implement(self,pos,dir):
        if dir == 0:
            self.rect.bottomright = pos
        if dir == 180:
            self.rect.bottomleft = pos
        self.exist = True
    def out_width(self):
        self.rect.center = (-100,-100)
    def reset_cooldown(self):
        self.cooldown = 100
    def width_changing(self,pos):
        self.size += 1
        self.surf = pygame.Surface([self.size,self.size]).convert()
        self.rect = self.surf.get_rect()
        self.rect = pos
    def update(self,player,pos):
        if self.exist:
            print(1)
            self.width_changing(pos)
        if self.size > 100:
            self.size = 1
            self.surf = pygame.Surface([self.size,self.size]).convert()
            self.rect = self.surf.get_rect()
            self.out_width()
            self.exist = False
        self.cooldown_creasing()
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1
