from typing import Tuple
import pygame as py
import sys
from Platform import *
from Test_plat import *
from pygame.constants import K_k
from character import *
from BG import background_test
from all_menu.setting_menu import Setting_menu
from character2.fireball import fireball
from main_menu import main_Menu
from all_of_generate import all_generate
from auto_cannon import Auto_cannon
from character1.player1 import *
from character2.player2 import player2
class first():
    def __init__(self):
        #self.player = player1("cats", 150, 150, "character1/L-walk1.png")
        self.player = player2("cats", 150, 150, "character1/L-walk1.png")
        self.main_Platform_1 = platform(1200, 20, 255, 0, 0, 50, 150, 700)
        self.float_plat_1 = platform(100, 30, 255, 0, 0, 50, 300, 650)
        self.float_plat_2 = platform(100, 30, 255, 0, 0, 50, 450, 600)
        self.float_plat_3 = platform(100, 30, 255, 0, 0, 50, 600, 650)
        self.bg = background_test()
        self.test=test_plat(100, 30, 255, 0, 0, 50, x=900, y=700,cnt=150,v=6,dir=2)
        self.test2=test_plat(30, 150, 255, 0, 0, 50, x=900, y=700,cnt=150,v=6,dir=1)
        self.cannon = Auto_cannon(100)
        self.all_gener = all_generate()
        self.move_x = None
        self.move_y = None
        #group
        self.move_plat=py.sprite.Group()
        self.can_go_down = py.sprite.Group()
        self.all_sprites_Group = py.sprite.Group()
        self.hitbox_group = py.sprite.Group()
        self.platforms_group = py.sprite.Group()
        self.weapon_group = py.sprite.Group()
        self.charater_group = py.sprite.Group()
        self.bullet_group = py.sprite.Group()
    def init_group(self):
        self.charater_group.add(self.player)
        self.move_plat.add(self.test)
        self.move_plat.add(self.test2)
        self.can_go_down.add(self.float_plat_1)
        self.can_go_down.add(self.float_plat_2)
        self.platforms_group.add(self.main_Platform_1)
        self.platforms_group.add(self.float_plat_1)
        self.platforms_group.add(self.float_plat_2)
        self.platforms_group.add(self.float_plat_3)
        self.platforms_group.add(self.test)
        self.platforms_group.add(self.test2)
        self.all_sprites_Group.add(self.bg)
        self.all_sprites_Group.add(self.player)
        self.all_sprites_Group.add(self.float_plat_1)
        self.all_sprites_Group.add(self.main_Platform_1)
        self.all_sprites_Group.add(self.float_plat_2)
    def init_factor(self):
        self.init_group()
        self.all_gener.declear()
    def action(self):
        self.bullet_group.update(self.player,self.bullet_group)
        self.move_x,self.move_y = self.player.move_position()
        self.all_gener.update(self.player,self.platforms_group)
        self.player.blood.update()
        self.player.key_board_get()
        self.player.movement(self.main_Platform_1, self.platforms_group, self.can_go_down,self.bullet_group)
        self.player.key_gets()
        self.player.using_skill(self.platforms_group)
        self.cannon.aim_target_rotating(self.player.pos)
        self.cannon.shooting(self.bullet_group,self.player.pos) 
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
        background.blit(self.cannon.player_rotated,self.cannon.player_rotated_rect)
        background.blit(self.main_Platform_1.image,self.main_Platform_1.rect)
        background.blit(self.float_plat_1.image,self.float_plat_1.rect)
        background.blit(self.float_plat_2.image,self.float_plat_2.rect)
        background.blit(self.float_plat_3.image,self.float_plat_3.rect)
        self.player.bliting(background)
        