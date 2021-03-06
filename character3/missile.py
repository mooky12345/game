import pygame
from pygame import image
from character3.explosion import explosion
import math
import random

class missile():
    def __init__(self,player):
        pygame.sprite.Sprite.__init__(self)
        # self.surf = pygame.Surface([60,60]).convert()
        # self.surf.fill((0,0,0,0))
        self.surf = pygame.image.load("missile/missile.jpg").convert_alpha()
        self.surf=pygame.transform.scale(self.surf,(60,60))
        self.rect = self.surf.get_rect()
        self.rect.center = (-100,-100)
        self.cooldown = 300
        self.max_cooldown = 300
        self.explosion_cooldown = 400
        self.direction = 180
        self.exist = False 
        self.speed = 3
        self.pos = [-100,-100]
        self.target_player = None
        self.explosion = explosion()
        self.player_rotated = None
        self.player_rotated_rect = None
    def implement(self,players,dir):
        self.direction = dir
        if self.cooldown == 0:
            self.target_player = self.randon_player(players)
            self.target_player = players[0]
            self.exist = True
            self.cooldown = 300
            if self.direction == 0:
                self.rect.topleft = (0,0)
                self.pos[0] = 100
                self.pos[1] = 100
            if self.direction == 180:
                self.rect.topleft = (0,0)
                self.pos[0] = 100
                self.pos[1] = 100
    def out_width(self):
        self.rect.center = (-100,-100)
        self.pos[0] = -100
        self.pos[1] = -100
    def reset_cooldown(self):
        self.cooldown = 300
    def update(self,players,platfrom):
        if self.exist:
            angle = (180-math.degrees(math.atan2((self.target_player.pos[1]-self.rect.center[1]),(self.target_player.pos[0]-self.rect.center[0]))))
            self.pos[0] -= self.speed*math.cos(math.radians(angle))
            self.pos[1] += self.speed*math.sin(math.radians(angle))
            if pygame.sprite.spritecollide(self,players,False):
                hits = pygame.sprite.spritecollide(self,players,False)

                self.exist = False
                self.explosion.implement(self.rect.bottomleft,self.direction)
                self.out_width()
                self.explosion_cooldown = 300
                for player in hits:
                    if player.name == "3":
                        continue
                    player.blood.cut_blood(20,True)
                    player.knock_back(self.rect.center,10,40)
            if  self.explosion_cooldown == 100:
                pass
            if  self.explosion_cooldown == 0:
                self.exist = False
                self.explosion.implement(self.rect.bottomleft,self.direction)
                self.explosion.implement(self.rect.bottomleft,self.direction)
                self.explosion_cooldown = 300
                self.out_width()
            self.explosion_cooldown_creasing()
            self.rect.topleft = self.pos
            self.aim_target_rotating(self.target_player.pos)
        self.explosion.update(players)
        self.cooldown_creasing()
    def randon_player(self,players):
        player = random.choice(players)
        while player.name == "3":
            player = random.choice(players)
        return player
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -= 1
    def explosion_cooldown_creasing(self):
        if self.explosion_cooldown > 0:
            self.explosion_cooldown -=1
    def rotated(self,surface,angle):
        rotate_surface = pygame.transform.rotozoom(surface,angle,1)
        return  rotate_surface
    def get_angle(self,pos):#down to 0, right to 90
        return (360-math.degrees(math.atan2((self.target_player.pos[1]-self.rect.center[1]),(self.target_player.pos[0]-self.rect.center[0])))) 
    def aim_target_rotating(self,pos):
        angle = self.get_angle(pos)+4
        self.player_rotated = self.rotated(self.surf,angle)      
    def knock_back(player,dir):
        pass