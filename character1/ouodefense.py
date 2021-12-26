from genericpath import exists
import pygame
class ouodefense(pygame.sprite.Sprite):
    def __init__(self):
        self.surf = pygame.Surface([30,120]).convert()
        self.surf.fill((0,0,0,100))
        self.rect = self.surf.get_rect()
        self.rect.center = (-100,-100)
        self.cooldown = 100
        self.exist = False
        self.max_cooldown = 100
        self.direction = None
        self.record_blood = None
    def implement(self,pos,player):
        if self.cooldown == 0:
            self.exist = True
            self.record_blood = player.blood.blood
            if self.direction == 0:
                self.rect.bottomleft = (pos[0]+30,pos[1])
            if self.direction == 180:
                self.rect.bottomleft = (pos[0]-30,pos[1])
    def out_width(self):
        self.exist = False
        self.rect.center = (-100,-100)
    def reset_cooldown(self):
        self.cooldown = 100
    def update(self,dir,bullet,player):
        if self.exist:
            player.blood.blood = self.record_blood
        self.direction = dir
        hit = pygame.sprite.spritecollide(self, bullet, False)
        for item in hit:
            item.kill()
        self.cooldown_creasing()
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1