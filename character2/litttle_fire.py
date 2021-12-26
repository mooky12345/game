import pygame
from pygame import sprite
import os
import random 
class little_fireball(pygame.sprite.Sprite):
    def __init__(self,pos,dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20]).convert_alpha()
        self.image.fill((0,255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (-100,-100)
        self.cooldown = 200
        self.direction = dir
        self.vel = [random.uniform(3,10),random.uniform(3,10)]     
        self.init_pos(pos)
        self.x=0
        image_path="fire"
        self.temp_list = []
        self.number_of_frames = len(os.listdir(image_path))
        print(self.number_of_frames)
        for i in range(1, self.number_of_frames + 1):
            img = image_path+"/{}.png".format(i)
            self.temp_list.append(img)
        self.pictures=[]
        for i in self.temp_list:
            picture=pygame.image.load(i).convert_alpha()
            picture=pygame.transform.scale(picture,(20,20)).convert_alpha()
            self.pictures.append(picture)
            
    def init_pos(self,pos):
        self.rect.center = pos
    def update(self,players,platforms):
        if self.x>18:
            self.x=0
        self.x+=1
        self.image.blit(self.pictures[self.x],(0,0))
        if pygame.sprite.spritecollide(self,players,False):
            hits=pygame.sprite.spritecollide(self,players,False)
            for player in hits:
                player.blood.cut_blood(0.3,True)
        if self.cooldown == 0:
            self.kill()
        if self.direction == 0:
            self.rect.x += self.vel[0] 
        if self.direction == 180:
            self.rect.x -= self.vel[0] 
        if pygame.sprite.spritecollide(self,platforms,False):
            self.vel[1] = 0
            self.vel[0] = 0
        self.rect.y -= self.vel[1]
        self.vel[1] -= 0.5
        self.cooldown_creasing()
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1