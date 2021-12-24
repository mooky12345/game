import pygame
class explosion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = 3
        self.surf = pygame.Surface([self.size,self.size]).convert()
        self.surf.fill((0,255,0,100))
        self.rect = self.surf.get_rect()
        self.rect.center = (100,100)
        self.cooldown = 100
        self.direction = None
        self.exist = False 
        self.pos = [-100,-100]
    def implement(self,pos,dir):
        if dir == 0:
            self.pos = pos
        if dir == 180: 
            self.pos = pos
        self.exist = True
    def out_width(self):
        self.rect.center = (-100,-100)
    def reset_cooldown(self):
        self.cooldown = 100
    def width_changing(self):
        self.size += 1
        self.surf = pygame.Surface([self.size,self.size]).convert()
        self.rect = self.surf.get_rect()
        self.rect.center = self.pos
    def update(self,player):
        if pygame.sprite.spritecollide(self,player,False):
            hits =pygame.sprite.spritecollide(self,player,False)
            for player in hits:
                player.blood.cut_blood(20,True)
                player.knock_back()
        if self.exist:
            self.width_changing()
        if self.size > 100:
            self.size = 3
            self.surf = pygame.Surface([self.size,self.size]).convert()
            self.rect = self.surf.get_rect()
            self.out_width()
            self.exist = False
        self.rect.bottomleft = self.pos
        self.cooldown_creasing()
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1
