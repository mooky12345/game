import pygame
from pygame import sprite
from character2.explosion import explosion
from character2.litttle_fire import little_fireball

class fireball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface([60,60]).convert()
        self.surf.fill((0,0,0,100))
        self.rect = self.surf.get_rect()
        self.rect.center = (-100,-100)
        self.cooldown = 200
        self.direction = None
        self.exist = False 
        self.littlefire_group = pygame.sprite.Group()
        self.explosion = explosion()
        self.max_cooldown=200
    def implement(self,pos,dir):
        self.direction = dir
        if self.cooldown == 0:
            self.cooldown=self.max_cooldown
            self.exist = True
            if self.direction == 0:
                self.rect.bottomleft = (pos[0]+31,pos[1])
            if self.direction == 180:
                self.rect.bottomright = (pos[0]-1,pos[1])
    def out_width(self):
        self.rect.center = (-100,-100)
    def reset_cooldown(self):
        self.cooldown = self.max_cooldown
    def update(self,player,platform):
        if pygame.sprite.spritecollide(self,player,False):
            hits=pygame.sprite.spritecollide(self,player,False)
            for player in hits:
                player.knock_back()
                player.blood.cut_blood(15,True)
        if self.exist:
            if self.direction == 0:
                self.rect.bottom += 10
                self.rect.right += 10
            if self.direction == 180:
                self.rect.bottom += 10
                self.rect.right -= 10
            # if pygame.sprite.spritecollide(self,player,False):
            #     self.exist = False
            #     if self.direction == 0:
            #         self.explosion.implement(self.rect.bottomright)
            #     if self.direction == 180:
            #         self.explosion.implement(self.rect.bottomleft)
            #     player.cut_blood(10,1)
            #     self.littlefire_generate(self.rect.center)
            #     self.out_width()
            if pygame.sprite.spritecollide(self,platform,False):
                self.exist = False
                if self.direction == 0:
                    self.explosion.implement(self.rect.bottomright,self.direction)
                if self.direction == 180:
                    self.explosion.implement(self.rect.bottomleft,self.direction)
                self.littlefire_generate(self.rect.center)
                self.out_width()
        self.littlefire_group.update(player,platform)
        self.explosion.update(player)
        self.cooldown_creasing()
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1
    def littlefire_generate(self,pos):
        for _ in range(5):
            fire = little_fireball(pos,180)
            self.littlefire_group.add(fire)
        for _ in range(5):
            fire = little_fireball(pos,0)
            self.littlefire_group.add(fire)
    