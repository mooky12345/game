from character import *
from character1.ouodefense import *
from character1.ouofoot import ouofoot
from character1.ouohand import ouohand
from persons_skill_cool_bar import cool_bar
import pygame
width=1500
class player1(Character):
    def __init__(self, name, cx, cy, image_path,player_group):
        super().__init__(name, cx, cy, image_path,player_group)
        self.keys = pygame.key.get_pressed()
        self.ouohand = ouohand()
        self.ouofoot = ouofoot()
        self.hand_defense =  ouodefense()
        self.cool_bar = cool_bar(src="player_1")
        self.ouohand_ret = False
        self.ouohand_pre_ret = False
        self.hand_defense_ret = False
        self.hand_defense_pre_ret = False
        self.ouofoot_ret = False
        self.ouofoot_pre_ret = False 
    def defense(self,bullet_gruop):
        if self.hand_defense_ret and self.hand_defense.cooldown == 0:
            self.moving_ret = False
            self.hand_defense.implement(self.pos,self)
        if self.hand_defense_pre_ret and not self.hand_defense_ret:
            self.moving_ret = True
            self.hand_defense.reset_cooldown()
            self.hand_defense.out_width() 
        self.hand_defense.update(self.direction,bullet_gruop,self)
    def The_ouohand(self):
        if not self.ouohand_pre_ret and self.ouohand_ret:
            self.ouohand.implement(self.pos,self.direction)
        self.ouohand.update(self.player_group)
    def The_ouofoot(self):
        if not self.ouofoot_pre_ret and self.ouofoot_ret:
            self.ouofoot.implement(self.pos,self.direction,self.rect)
        self.ouofoot.update(self.rect,self.player_group)
    def key_gets(self,event):
        self.hand_defense_pre_ret = self.hand_defense_ret
        self.ouohand_pre_ret = self.ouohand_ret
        self.ouofoot_pre_ret = self.ouofoot_ret
        try:
            if event.button == 1 and event.type == JOYBUTTONDOWN:
                self.hand_defense_ret = True
            elif event.button == 1 and event.type == JOYBUTTONUP:
                self.hand_defense_ret = False
            if event.button == 2 and event.type == JOYBUTTONDOWN:
                self.ouohand_ret = True
            elif event.button == 2 and event.type == JOYBUTTONUP:
                self.ouohand_ret = False
            if event.button == 3 and event.type == JOYBUTTONDOWN:
                self.ouofoot_ret = True
            elif event.button == 3 and event.type == JOYBUTTONUP:
                self.ouofoot_ret = False
        except AttributeError:
            return
    def cooldowm_bar(self):
        a,b,c=self.return_cooldown()  #1231231213
        m1,m2,m3=self.return_max_cooldown()
        arc =round(float(1-a/m1)*360,1)-90
        arc2=round(float(1-b/m2)*360,1)-90
        arc3=round(float(1-c/m3)*360,1)-90
        self.cool_bar.update(arc=arc,arc2=arc2,arc3=arc3)
    def using_skill(self,platform,bullet_group):
        self.cooldowm_bar()
        self.defense(bullet_group)
        self.The_ouohand()
        self.The_ouofoot()
    def return_cooldown(self):
        return self.ouohand.cooldown, self.ouofoot.cooldown, self.hand_defense.cooldown
    def return_max_cooldown(self):
        return self.ouohand.max_cooldown,self.ouofoot.max_cooldown ,self.hand_defense.max_cooldown
    def bliting(self,background):
        background.blit(self.surf,self.rect)
        background.blit(self.ouohand.surf,self.ouohand.rect)
        background.blit(self.ouofoot.surf,self.ouofoot.rect)      
        background.blit(self.hand_defense.surf,self.hand_defense.rect)
        background.blit(self.cool_bar.surf,(width-150,0))
        background.blit(self.normal_attack_image.surf,self.normal_attack_image.rect)
        background.blit(self.shield_image.image,self.shield_image.rect)
        if self.get_weapon != None:
            image = pygame.image.load(self.get_weapon.image).convert_alpha()
            image = pygame.transform.scale(image, (30,30))
            background.blit(image,(1200,0))
        background.blit(self.blood.surf, (0,0))

    