from character import Character
from ouodefense import ouodefense
from ouofoot import ouofoot
from ouohand import ouohand
import pygame
class player1(Character):
    def __init__(self, name, cx, cy, image_path):
        super().__init__(name, cx, cy, image_path)
        self.keys = pygame.key.get_pressed()
        self.hand = ouohand()
        self.foot = ouofoot()
        self.hand_defense =  ouodefense()
        self.hand_defense_ret = False
        self.hand_defense_pre_ret = False
    def defense(self):
        if self.hand_defense_pre_ret and not self.hand_defense_ret:
            ouodefense.reset_cooldown()
            ouodefense.out_width()
        ouodefense.cooldown_creasing()
    def The_ouohand(self):
        pass
    def The_ouofoot(self):
        pass
    def key_gets(self):
        self.hand_defense_pre_ret = self.hand_defense_ret
        if self.keys[pygame.K_y]:
            self.hand_defense_ret = True
        else:
            self.hand_defense_ret = False
        if self.keys[pygame.K_u]:
            pass
        if self.keys[pygame.K_i]:
            pass
    
    def using_skill(self):
        pass
