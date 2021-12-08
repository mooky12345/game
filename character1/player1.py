from character import *
from character1.ouodefense import *
from character1.ouofoot import ouofoot
from character1.ouohand import ouohand
import pygame
class player1(Character):
    def __init__(self, name, cx, cy, image_path):
        super().__init__(name, cx, cy, image_path)
        self.keys = pygame.key.get_pressed()
        self.ouohand = ouohand()
        self.ouofoot = ouofoot()
        self.hand_defense =  ouodefense()
        self.ouohand_ret = False
        self.ouohand_pre_ret = False
        self.hand_defense_ret = False
        self.hand_defense_pre_ret = False
        self.ouofoot_ret = False
        self.ouofoot_pre_ret = False 
    def defense(self):
        if self.hand_defense_ret:
            self.stop_moving()
            self.hand_defense.implement(self.pos)
        if self.hand_defense_pre_ret and not self.hand_defense_ret:
            self.hand_defense.reset_cooldown()
            self.hand_defense.out_width() 
        self.hand_defense.update(self.direction)
    def stop_moving(self):
        self.vel = (0,0)
    def The_ouohand(self):
        if not self.ouohand_pre_ret and self.ouohand_ret:
            self.ouohand.implement(self.pos)
        self.ouohand.update(self.direction)
    def The_ouofoot(self):
        if not self.ouohand_pre_ret and self.ouohand_ret:
            self.ouofoot.implement(self.pos)
        self.ouofoot.update(self.pos,self.direction)
    def key_gets(self):
        self.hand_defense_pre_ret = self.hand_defense_ret
        self.ouohand_pre_ret = self.ouohand_ret
        self.ouofoot_pre_ret = self.ouofoot_ret
        if self.keys[pygame.K_y]:
            self.hand_defense_ret = True
        else:
            self.hand_defense_ret = False
        if self.keys[pygame.K_u]:
            self.ouohand_ret = True
        else:
            self.ouohand_ret = False
        if self.keys[pygame.K_i]:
            self.ouofoot_ret = True
        else:
            self.ouofoot_ret = False
    def using_skill(self):
        self.defense()
        self.The_ouohand()
        self.The_ouofoot()
