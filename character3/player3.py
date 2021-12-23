from pygame.constants import JOYBUTTONDOWN, JOYBUTTONUP
from character import Character
from character3.missile import missile
from character3.toxic import toxic
import pygame


class player3(Character):
    def __init__(self, name, cx, cy, image_path):
        super().__init__(name, cx, cy, image_path)
        self.missile_ret = False
        self.missile_pre_ret = False
        self.shoting_missile = missile(self)
        self.toxic_ret = False
        self.toxic_pre_ret = False
        self.toxic_shoot = toxic()
    def toxic_shooting(self,bullet_group):
        pass
        if self.toxic_ret and not self.toxic_pre_ret:
            self.toxic_shoot.implement(bullet_group,self.own_bullet_group,self.direction)
        self.shoting_missile.update(self)
    def shooting_missile(self):
        if self.missile_ret and not self.missile_pre_ret:
            self.shoting_missile.implement(self.pos,self.direction)
        self.shoting_missile.update(self)
    def key_gets(self,event):
        self.missile_pre_ret = self.missile_ret
        self.toxic_pre_ret = self.toxic_ret
        try:
            if event.button == 1 and event.type == JOYBUTTONDOWN:
                self.missile_ret = True
            elif event.button == 1 and event.type == JOYBUTTONUP:
                self.missile_ret = False
            if event.button == 2 and event.type == JOYBUTTONDOWN:
                self.toxic_ret = True
            elif event.button == 2 and event.type == JOYBUTTONUP:
                self.toxic_ret = False
        except AttributeError:
            return
    def using_skill(self,platfrom,bullet_group):
        self.shooting_missile()
        self.toxic_shoot(bullet_group)
    def bliting(self,background):
        background.blit(self.surf,self.rect)
        background.blit(self.blood.surf, (0,0))
        background.blit(self.shield_image.image,self.shield_image.rect)
        background.blit(self.surf,self.rect)
        background.blit(self.shoting_missile.surf,self.shoting_missile.rect)
        background.blit(self.shoting_missile.explosion.surf,self.shoting_missile.explosion.rect)