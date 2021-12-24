from typing import Tuple
import pygame as py
import sys
from Platform import platform
from Test_plat import *
from pygame.constants import K_k
from character import *
from BG import  background_test
from all_menu.setting_menu import Setting_menu
from character2.fireball import fireball
from main_menu import main_Menu
from all_of_generate import all_generate
from auto_cannon import Auto_cannon
from character1.player1 import *
from character2.player2 import player2
from character3.player3 import player3
from persons_skill_cool_bar import cool_bar
from select_player_number import select_role_number_screen
import random
width=1500
height=800
class first():
    def __init__(self,player_cnt,player_list):
        self.player_cnt = player_cnt
        self.cool_bar=cool_bar(src="player_1")
        self.main_Platform_1 = platform(1200, 20, 255, 0, 0, 50, 150, 700)
        self.float_plat_1 = platform(100, 30, 255, 0, 0, 50, 300, 650)
        self.float_plat_2 = platform(100, 30, 255, 0, 0, 50, 450, 600)
        self.float_plat_3 = platform(100, 30, 255, 0, 0, 50, 600, 650)
        self.bg = background_test()
        self.test=test_plat(100, 30, 255, 0, 0, 50, x=900, y=700,cnt=150,v=6,dir=2)
        self.test2=test_plat(30, 150, 255, 0, 0, 50, x=900, y=700,cnt=150,v=6,dir=1)
        self.cannon = Auto_cannon(100)
        self.all_gener = all_generate()
        self.player_own_play_list = player_list
        self.joyevent = None
        self.move_x = None
        self.move_y = None
        #group
        self.move_plat=py.sprite.Group()
        self.can_go_down = py.sprite.Group()
        self.all_sprites_Group = py.sprite.Group()
        self.hitbox_group = py.sprite.Group()
        self.platforms_group = py.sprite.Group()
        self.weapon_group = py.sprite.Group()
        self.player_group = py.sprite.Group()
        self.bullet_group = py.sprite.Group()
    def init_group(self):
        self.move_plat.add(self.test)
        self.move_plat.add(self.test2)
        self.can_go_down.add(self.float_plat_1)
        self.can_go_down.add(self.float_plat_2)
        self.can_go_down.add(self.float_plat_3)
        self.platforms_group.add(self.main_Platform_1)
        self.platforms_group.add(self.float_plat_1)
        self.platforms_group.add(self.float_plat_2)
        self.platforms_group.add(self.float_plat_3)
        self.platforms_group.add(self.test)
        self.platforms_group.add(self.test2)
        self.all_sprites_Group.add(self.bg)
        self.all_sprites_Group.add(self.float_plat_1)
        self.all_sprites_Group.add(self.main_Platform_1)
        self.all_sprites_Group.add(self.float_plat_2)
        for player in self.player_own_play_list:
            self.player_group.add(player)
    def init_player(self):
        for item in range(self.player_cnt):
            self.player_own_play_list[item] = self.player_own_play_list[item].name
    def init_player_object(self):
        for item in range(self.player_cnt):
            if self.player_own_play_list[item] == "1":
                self.player_own_play_list[item] = player1("1", 900, 150, "character1/L-walk1.png",self.player_own_play_list)
            if self.player_own_play_list[item] == "2":
                self.player_own_play_list[item] = player2("2", 600, 150, "character1/L-walk1.png",self.player_own_play_list)
            if self.player_own_play_list[item] == "3":
                self.player_own_play_list[item] = player3("3", 300, 150, "character1/L-walk1.png",self.player_own_play_list)
    def init_factor(self):
        self.init_player()
        self.init_player_object()
        self.init_group()
        self.all_gener.declear()
    def getjoystick_event(self,event):
        if event == 0:
            for player in self.player_own_play_list:
                player.keyboard_control(event)
                player.key_gets(event)
                self.all_gener.update(self.player_own_play_list[0],self.platforms_group,event)
            return 
        for index in range(self.player_cnt):
            if event.joy == index:
                self.player_own_play_list[index].keyboard_control(event)
                self.player_own_play_list[index].key_gets(event)
                self.all_gener.update(self.player_own_play_list[index],self.platforms_group,event)
      
    def action(self):
        self.bullet_group.update(self.player_group,self.bullet_group)
        self.move_x,self.move_y = self.player_own_play_list[0].move_position()
        for player in self.player_own_play_list:
            player.blood.update()
            player.movement(self.main_Platform_1, self.platforms_group, self.can_go_down,self.bullet_group)
            player.using_skill(self.bullet_group,self.platforms_group)
        pos = self.random_pos()
        # self.cannon.aim_target_rotating()
        # self.cannon.shooting(self.bullet_group,pos) 
    def bliting(self,background):
        background.fill((0, 0, 0))
        background.blit(self.bg.surf, self.bg.rect)
        self.bullet_group.draw(background)
        for entity in self.all_gener.generator:
            background.blit(entity.surf, entity.rect)
        for entity in self.move_plat:
            entity.plat_redraw(self.move_x,self.move_y,entity.x/2,entity.y)
        for entity in self.move_plat:
            background.blit(entity.image, entity.rect)
        
        background.blit(self.main_Platform_1.image,self.main_Platform_1.rect)
        background.blit(self.float_plat_1.image,self.float_plat_1.rect)
        background.blit(self.float_plat_2.image,self.float_plat_2.rect)
        background.blit(self.float_plat_3.image,self.float_plat_3.rect)
        #self.cannon.bliting(background)
        for player in self.player_own_play_list:
            player.bliting(background)
    def random_pos(self):
        return (random.randint(0,width),random.randint(1,height))