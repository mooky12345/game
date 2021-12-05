import pygame
import math
from pygame import surface
from main import background
from bullet import Bullet
class Auto_cannon(pygame.sprite.Sprite):
    def __init__(self,radium):
        super().__init__()
        self.image = pygame.Surface([radium*2,radium*2]).convert_alpha()
        self.rect.center = (750,0)
        self.image.fill((0,0,0,0))
        pygame.draw.rect(self.image, (255,255,0,100), (radium,radium,20,radium*2),0)#pygame.draw.rect(畫布, 顏色, [x坐標, y坐標, 寬度, 高度], 線寬)
        pygame.draw.circle(self.image, (255,255,0,100), (radium,radium), radium/2)
    def blit_base(self):
        background.blit(self.image,self.rect)
    def shooting(self,bullet_group):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 50
            bullet = Bullet(self.rect.centerx + (math.cos(math.degrees(self.direction))*5),
            self.rect.centery - (math.cos(math.degrees(self.direction))*5), self.direction)
            bullet_group.add(bullet)
    def aim_rotating(self,player_pos):
        pass
    
