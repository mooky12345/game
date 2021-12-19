import pygame
from pygame.constants import JOYBUTTONDOWN, JOYBUTTONUP
from character import Character
from character2.fireball import *
from character2.transport_damage import transport_damage 
class player2(Character):
    def __init__(self, name, cx, cy, image_path):
        super().__init__(name, cx, cy, image_path)
        self.shooting_fireball_ret = False
        self.transporting_damage_ret = False
        self.shooting_fireball_pre_ret = False
        self.transporting_damage_pre_ret = False
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
        print( self.transporting_damage_ret )
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
    def using_skill(self,platform):
        self.shooting_fireball(platform)
        self.transporting_damage()
    def bliting(self,background):
        background.blit(self.surf,self.rect)
        background.blit(self.trans_damage.surf1,self.trans_damage.rect1)
        background.blit(self.trans_damage.surf2,self.trans_damage.rect2)
        background.blit(self.fireball.surf,self.fireball.rect)
        background.blit(self.fireball.explosion.surf,self.fireball.explosion.rect)
        self.fireball.littlefire_group.draw(background)
        background.blit(self.shield_image.image,self.shield_image.rect)
        background.blit(self.normal_attack_image.surf,self.normal_attack_image.rect)
        background.blit(self.blood.surf, (0,0))