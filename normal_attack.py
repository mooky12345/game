from genericpath import exists
import pygame
class normal_attack(pygame.sprite.Sprite):
    def __init__(self):
        self.surf = pygame.Surface([130,30]).convert()
        self.surf.fill((0,0,0,100))
        self.rect = self.surf.get_rect()
        self.rect.center = (-100,-100)
        self.direction = None
        self.exist = False
        self.speed = 10
        self.cooldown = 100
        self.exist_cooldown = 3
    def implement(self,dir,pos):
        self.direction = dir
        self.exist = True
        if self.direction == 0:
            self.rect.left = pos[0]+32
            self.rect.top = pos[1]-60
        if self.direction == 180:
            self.rect.right = pos[0]-2
            self.rect.top = pos[1]-60
    def update(self,players,name):
        if self.cooldown > 0:
            self.cooldown -= 1
        if self.exist:
            self.exist_cooldown -= 1
            if pygame.sprite.spritecollide(self,players,False):
                hits = pygame.sprite.spritecollide(self,players,False)
                for player in hits:
                    if player.name == name:
                        continue
                    else:
                        player.blood.cut_blood(10,1)
                        player.knock_back(self.rect.center,1,40)
            if self.exist_cooldown < 0:
                self.exist_cooldown = 3
                self.exist = False
                self.rect.center = (-100,-100)
            
