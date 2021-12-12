import pygame
from explosion import explosion
class missile():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface([60,60]).convert()
        self.surf.fill((0,0,0,100))
        self.rect = self.surf.get_rect()
        self.rect.center = (-100,-100)
        self.cooldown = 300
        self.explosion_cooldown = 200
        self.direction = None
        self.exist = False 
        self.explosion = explosion()
    def implement(self,pos,dir):
        self.direction = dir
        if self.cooldown == 0:
            self.exist = True
            if self.direction == 0:
                self.rect.bottomleft = (pos[0]+31,pos[1])
            if self.direction == 180:
                self.rect.bottomright = (pos[0]-1,pos[1])
    def out_width(self):
        self.rect.center = (-100,-100)
    def reset_cooldown(self):
        self.cooldown = 300
    def update(self,player):
        if self.exist:
            if self.direction == 0:
                self.rect.bottomright += 10
            if self.direction == 180:
                self.rect.bottom += 10
                self.rect.right -= 10
            if pygame.sprite.spritecollide(self,player):
                self.exist = False
                self.explosion.implement(self.rect.bottomleft)
                player.cut_blood(10,1)
                self.out_width()
            if  self.explosion_cooldown == 0:
                self.explosion.implement(self.rect.bottomleft)
                self.out_width()

        self.explosion.update()
        self.cooldown_creasing()
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1
    def knock_back(player,dir):
        pass