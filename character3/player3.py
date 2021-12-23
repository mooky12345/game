from pygame.constants import JOYBUTTONDOWN, JOYBUTTONUP
from character import Character
from character3.missile import missile
from character3.toxic import toxic
from persons_skill_cool_bar import cool_bar
import pygame

width = 1500
class player3(Character):
    def __init__(self, name, cx, cy, image_path):
        super().__init__(name, cx, cy, image_path)
        self.missile_ret = False
        self.missile_pre_ret = False
        self.shoting_missile = missile(self)
        self.toxic_ret = False
        self.toxic_pre_ret = False
        self.toxic_shoot = toxic()
        self.cool_bar = cool_bar(src="player_1")
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
        self.cooldowm_bar()
        self.shooting_missile()
        self.toxic_shooting(bullet_group)
    def bliting(self,background):
        background.blit(self.surf,self.rect)
        background.blit(self.blood.surf, (0,60))
        background.blit(self.shield_image.image,self.shield_image.rect)
        background.blit(self.cool_bar.surf,(width-150,60))
        background.blit(self.surf,self.rect)
        background.blit(self.shoting_missile.surf,self.shoting_missile.rect)
        background.blit(self.shoting_missile.explosion.surf,self.shoting_missile.explosion.rect)
    def return_cooldown(self):
        return self.shoting_missile.cooldown,self.toxic_shoot.cooldown
    def return_max_cooldown(self):
        return self.shoting_missile.max_cooldown,self.toxic_shoot.max_cooldown
    def cooldowm_bar(self):
        a,b=self.return_cooldown()  #1231231213
        m1,m2=self.return_max_cooldown()
        arc =round(float(1-a/m1)*360,1)-90
        arc2=round(float(1-b/m2)*360,1)-90
        self.cool_bar.update(arc=arc,arc2=arc2)