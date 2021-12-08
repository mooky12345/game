from character import Character
from ouodefense import ouodefense
from ouofoot import ouofoot
from ouohand import ouohand
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
            ouodefense.implement(self.pos,self.direction)
        if self.hand_defense_pre_ret and not self.hand_defense_ret:
            ouodefense.reset_cooldown()
            ouodefense.out_width() 
        ouodefense.update()
    def The_ouohand(self):
        if not self.ouohand_pre_ret and self.ouohand_ret:
            ouohand.implement(self.pos,self.direction)
        ouohand.update()
    def The_ouofoot(self):
        if not self.ouohand_pre_ret and self.ouohand_ret:
            ouofoot.implement(self.pos)
        ouofoot.update()
    def key_gets(self):
        self.hand_defense_pre_ret = self.hand_defense_ret
        self.ouohand_pre_ret = self.ouohand_ret
        self.ouofoot_pre_ret = self.ouufoot_ret
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
