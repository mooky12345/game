import pygame
from character import Character
from fireball import fireball
from transport_damage import transport_damage 
class player2(Character):
    def __init__(self, name, cx, cy, image_path):
        super().__init__(name, cx, cy, image_path)
        self.shooting_fireball_ret = False
        self.transporting_damage_ret = False
        self.shooting_fireball_pre_ret = False
        self.transporting_damage_pre_ret = False
        self.fireball = fireball()
        self.trans_damage = transport_damage()
    def shooting_fireball(self):
        if self.shooting_fireball_ret and not self.shooting_fireball_pre_ret:
            self.fireball.implement(self.pos,self.direction)
        self.fireball.update()
    def transporting_damage(self):
        if self.transporting_damage_ret and self.transporting_damage_pre_ret:
           self.trans_damage.implement(self.pos,self)
        self.trans_damage.update()
    def key_get(self):
        self.shooting_fireball_pre_ret = self.shooting_fireball_ret
        self.transporting_damage_pre_ret = self.transporting_damage_ret 
        if self.keys[pygame.K_y]:
            self.shooting_fireball_ret = True
        else:
            self.shooting_fireball_ret = False
        if self.keys[pygame.K_u]:
            self.transporting_damage_ret = True
        else:
            self.transporting_damage_pre_ret = False
       