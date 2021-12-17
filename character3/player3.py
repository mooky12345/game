from character import Character
from character3.missile import missile
import pygame
class player3(Character):
    def __init__(self, name, cx, cy, image_path):
        super().__init__(name, cx, cy, image_path)
        self.missile_ret = False
        self.missile_pre_ret = False
        self.shoting_missile = missile(self)
        self.toxic_ret = False
    def toxic_shooting(self):
        pass
    def shooting_missile(self):
        if self.missile_ret and not self.missile_pre_ret:
            self.shoting_missile.implement(self.pos,self.direction)
        self.shoting_missile.update(self)
    def key_gets(self):
        self.missile_pre_ret = self.missile_ret
        if self.keys[pygame.K_y]:
            self.missile_ret = True
        else:
            self.missile_ret = False
        if self.keys[pygame.K_u]:
            self.toxic_ret = True
        else:
            self.toxic_ret = False
    def using_skill(self):
        self.shooting_missile()
    def bliting(self,background):
        background.blit(self.surf,self.rect)
        background.blit(self.blood.surf, (0,0))
        background.blit(self.shield_image.image,self.shield_image.rect)
        background.blit(self.surf,self.rect)
        background.blit(self.shoting_missile.surf,self.shoting_missile.rect)
        background.blit(self.shoting_missile.explosion.surf,self.shoting_missile.explosion.rect)