import pygame

class explosion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = 1
        self.surf = pygame.Surface([self.size,self.size]).convert()
        self.surf.fill((0,0,0,100))
        self.rect = self.surf.get_rect()
        self.rect.center = (-100,-100)
        self.cooldown = 100
        self.direction = None
        self.exist = False 
        self.littlefire_group = pygame.sprite.group()
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
    def update(self,player,platform):
        if self.exist:
            self.size+=1
            if pygame.sprite.spritecollide(self,player):
                player.cut_blood(3,1)
        if self.size > 100:
            self.exist = False
        self.cooldown_creasing()
    
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1
