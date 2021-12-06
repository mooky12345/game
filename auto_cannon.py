import pygame
import math
from pygame import surface

from bullet import Bullet
class Auto_cannon(pygame.sprite.Sprite):
    def __init__(self,radium):
        super().__init__()
        self.image = pygame.Surface([radium*2,radium*2]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (750,0)
        self.image.fill((0,0,0,0))
        pygame.draw.rect(self.image, (255,255,0,100), (radium-10,radium-10,20,radium*2),0)#(畫布, 顏色, [x坐標, y坐標, 寬度, 高度], 線寬)
        pygame.draw.circle(self.image, (255,255,0,100), (radium,radium), radium/2)
        self.player_rotated = None
        self.player_rotated_rect = None
        self.shoot_cooldown = 5
    def shooting(self,bullet_group,pos):
        angle = self.get_angle(pos) + 270 +4
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 5
            bullet = Bullet(self.rect.centerx + (math.cos(angle)*5),
            self.rect.centery - (math.sin(angle)*5),angle)
            bullet_group.add(bullet)
    def rotated(self,surface,angle):
        rotate_surface = pygame.transform.rotozoom(surface,angle,1)
        rotate_rect = rotate_surface.get_rect(center=(750,0))
        return  rotate_surface,rotate_rect

    def get_angle(self,pos):#down to 0, right to 90
        return (90-math.degrees(math.atan2((pos[1]-self.rect.center[1]),(pos[0]-self.rect.center[0])))) 

    def aim_target_rotating(self,pos,background):
        try:
            angle = self.get_angle(pos)+4
        except ZeroDivisionError:
            pass
        self.player_rotated,self.player_rotated_rect = self.rotated(self.image,angle)
        background.blit(self.player_rotated,self.player_rotated_rect)
        

    
