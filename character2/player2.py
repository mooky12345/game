import pygame
from pygame.constants import JOYBUTTONDOWN, JOYBUTTONUP
from character import Character
from character2.fireball import *
from persons_skill_cool_bar import cool_bar
from character2.transport_damage import transport_damage 
width = 1500
class player2(Character):
    def __init__(self, name, cx, cy, image_path):
        super().__init__(name, cx, cy, image_path)
        self.shooting_fireball_ret = False
        self.transporting_damage_ret = False
        self.shooting_fireball_pre_ret = False
        self.transporting_damage_pre_ret = False
        self.cool_bar = cool_bar(src="player_1")
        self.fireball = fireball()
        self.trans_damage = transport_damage()
    def shooting_fireball(self,platform):
        if self.shooting_fireball_ret and not self.shooting_fireball_pre_ret:
            self.fireball.implement(self.pos,self.direction)
        self.fireball.update(self,platform)
    def transporting_damage(self):
        if self.transporting_damage_ret and self.transporting_damage_pre_ret:
           self.trans_damage.implement(self.pos,self)
        self.trans_damage.update()
    def key_gets(self,event):
        self.shooting_fireball_pre_ret = self.shooting_fireball_ret
        self.transporting_damage_pre_ret = self.transporting_damage_ret 
        
        try:
            if event.button == 1 and event.type == JOYBUTTONDOWN:
                self.shooting_fireball_ret = True
            elif event.button == 1 and event.type == JOYBUTTONUP:
                self.shooting_fireball_ret = False
            if event.button == 2 and event.type == JOYBUTTONDOWN:
                self.transporting_damage_ret = True
            elif event.button == 2 and event.type == JOYBUTTONUP:
                self.transporting_damage_ret = False
        except AttributeError:
            return
    def cooldowm_bar(self):
        a,b=self.return_cooldown()  #1231231213
        m1,m2=self.return_max_cooldown()
        arc =round(float(1-a/m1)*360,1)-90
        arc2=round(float(1-b/m2)*360,1)-90
        self.cool_bar.update(arc=arc,arc2=arc2)
    def using_skill(self,platform,bullet_group):
        self.shooting_fireball(platform)
        self.transporting_damage()
        self.cooldowm_bar()
    def bliting(self,background):
        background.blit(self.surf,self.rect)
        background.blit(self.cool_bar.surf,(width-150,30))
        background.blit(self.trans_damage.surf1,self.trans_damage.rect1)
        background.blit(self.trans_damage.surf2,self.trans_damage.rect2)
        background.blit(self.fireball.surf,self.fireball.rect)
        background.blit(self.fireball.explosion.surf,self.fireball.explosion.rect)
        self.fireball.littlefire_group.draw(background)
        background.blit(self.shield_image.image,self.shield_image.rect)
        background.blit(self.normal_attack_image.surf,self.normal_attack_image.rect)
        background.blit(self.blood.surf, (0,30))
    def return_cooldown(self):
        return self.fireball.cooldown,self.trans_damage.cooldown
    def return_max_cooldown(self):
        return self.fireball.max_cooldown,self.trans_damage.max_cooldown