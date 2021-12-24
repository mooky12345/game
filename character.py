import pygame
from genericpath import isfile
from pathlib import Path
import os
from pygame.event import event_name
from pygame.locals import *
from blood import bloodline
from bullet import Bullet
from shield import *
from persons_skill_cool_bar import cool_bar
from normal_attack import normal_attack
vec = pygame.math.Vector2
HEIGHT = 400
backgound_WIDTH = 900
ACC = 0.5
FRIC = -0.12
jump_speed = -13


class Character(pygame.sprite.Sprite):
    def __init__(self,name,cx,cy,image_path,player_group):
        super().__init__()
        self.player_group = player_group
        self.key_event = None
        self.normal_attack_ret = False
        self.normal_attack_pre_ret = False
        self.toxic_statement = False
        self.player_count = None 
        self.pre_shooting_ret = False
        self.shooting_ret = False
        self.get_weapon = None
        self.go_down_ground_button = False
        self.downcatch_right = True
        self.downcatch_left = True
        self.keys = pygame.key.get_pressed()
        self.squat_down = False
        self.squat_down_cnt = 0
        self.chwid = 30
        self.chhie = 60
        self.name = name
        self.pos = vec(cx,cy)
        self.moving_ret = True
        self.vel = vec(0, 0)
        self.acc = vec(0, 0.5)
        self.move_left_press = False
        self.move_right_press = False
        self.jump_button = False
        self.animation_list = []
        self.image_left_cnt = 0
        self.image_right_cnt = 0
        self.jump_count = 1
        self.pre_space = False
        self.squat_down_pre = False
        self.background_width = 900
        self.in_ack = False
        self.facing_right = True
        self.shoot_cooldown = 0
        self.ammo = 5
        self.weapon = 0
        self.hitbox = [self.pos.x + 20 , self.pos.y , 28 , 60]
        self.direction = 1
        self.get_shield_ret = False
        self.blit_shield_ret = False
        self.shield_image = Shield(50,(0,0,0),backgound_WIDTH/2,0)
        self.blood = bloodline()
        self.cnt =0
        self.normal_attack_image = normal_attack()
        self.own_bullet_group = pygame.sprite.Group()
        self.animation_type = {
            "Left_walk": 0,
            "Right_walk": 1,
            "Squat_down": 2
        }
        for animation in self.animation_type:
            temp_list = []
            number_of_frames = len(
                os.listdir("character1/{}".format(animation)))

            for i in range(1, number_of_frames + 1):
                img = "character1/{}/{}.png".format(animation, i)
                temp_list.append(img)

            self.animation_list.append(temp_list)
        self.charater_statement = image_path
        self.image = self.animation_list[self.animation_type["Left_walk"]][0]
        self.pre_image = self.animation_list[self.animation_type["Left_walk"]][
                self.image_left_cnt]
        self.image_varible_setter()

    def key_board_get(self):
        self.keys = pygame.key.get_pressed()

    def image_varible_setter(self):
        charImage = pygame.image.load(self.image)
        charImage = pygame.transform.scale(charImage, (self.chwid, self.chhie))
        self.rect = charImage.get_rect()
        self.rect.center = (1000,1000)
        self.surf = pygame.Surface((self.chwid, self.chhie))
        self.surf.blit(charImage, (0, 0))
    
    def image_reload(self):
        
        if self.squat_down:
            self.image = self.animation_list[self.animation_type["Squat_down"]][0]
            self.chhie = 30
        elif self.vel.x < 0:
            self.direction = 180
            self.image = self.animation_list[self.animation_type["Left_walk"]][
                self.image_left_cnt]
            self.image_left_cnt += 1
            if self.image_left_cnt >= len(self.animation_list[0]):
                self.image_left_cnt = 0
            self.pre_image = self.image
        elif self.vel.x > 0:
            self.direction = 0
            self.image = self.animation_list[
                self.animation_type["Right_walk"]][self.image_right_cnt]
            self.image_right_cnt += 1
            if self.image_right_cnt >= len(self.animation_list[1]):
                self.image_right_cnt = 0
            self.pre_image = self.image
        if not self.squat_down:
            self.chhie = 60
            self.image = self.pre_image
        
        
        self.image_varible_setter()
    def knock_back(self):
        pass
    def shoot(self,bullet_group):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        if self.get_weapon != None and self.get_weapon.image_weapon == "gun":
            if self.shoot_cooldown == 0 and self.get_weapon.count  > 0 and self.shooting_ret:
                self.shoot_cooldown = 20
                if self.direction == 0:
                    bullet = Bullet(self.rect.centerx + 50,self.rect.centery-5, self.direction,False)
                if self.direction == 180:
                    bullet = Bullet(self.rect.centerx - 50,self.rect.centery-5, self.direction,False)
                bullet_group.add(bullet)
                self.own_bullet_group.add(bullet)
                self.get_weapon.count -= 1
    def normal_attacking(self):
        if self.normal_attack_ret and not self.normal_attack_pre_ret and self.get_weapon != None:
            if self.get_weapon.image_weapon == "sword" and  self.get_weapon.count > 0 and self.normal_attack_image.cooldown == 0:
                self.normal_attack_image.cooldown = 100
                self.normal_attack_image.implement(self.direction,self.pos)
                self.get_weapon.count -= 1
        self.normal_attack_image.update()
    def disard_weapon(self):
        if self.get_weapon != None:
            try:
                if self.key_event.button == 5 and self.key_event.type == JOYBUTTONDOWN:
                    if self.get_weapon.count != 0:
                        self.get_weapon.rect.x,self.get_weapon.rect.y = self.pos.x,self.pos.y
                        self.get_weapon = None
                    else:
                        self.get_weapon.rect.x,self.get_weapon.rect.y = (-100,-100)
                        self.get_weapon = None
            except AttributeError:
                return
    def shield_broken(self,bullet):
        if self.get_shield_ret == True:
            if pygame.sprite.spritecollide(self.shield_image, bullet, False):
                if not pygame.sprite.spritecollide(self.shield_image, self.own_bullet_group, False):
                    hit = pygame.sprite.spritecollide(self.shield_image, bullet, False)
                    hit[0].kill()
                    self.get_shield_ret = False
    def pos_update(self, plat):
        if self.vel.y > 0:
            if self.go_down_ground_button:
                pass
            elif self.detect_hit(plat):
                pos = self.detect_hit(plat)
                if self.pos.y <= pos[0].rect.top+100:
                    self.vel.y = 0
                    self.pos.y = pos[0].rect.top + 1
                    self.jump_count = 1
        
    
       
    def detect_hit(self, platform_group):
        hits = pygame.sprite.spritecollide(self, platform_group, False)
        if hits:
            return hits
        else:
            return False   
    def speed_change(self, platforms, platform_group):
        self.walking_speed()
        self.jumping_speed(platform_group)
    def walking_speed(self):
        if self.move_left_press:
            self.acc.x = -ACC
        else:
            if self.move_right_press:
                self.acc.x = ACC
                
            else:
                self.acc.x = 0
                self.vel.x = 0
    
    def jumping_speed(self, platform_group):
      
        if not self.pre_space and self.jump_button:
       
            self.cnt += 1
            if self.on_ground():
                self.vel.y = jump_speed        
            elif self.jump_count > 0:
            
                self.vel.y = jump_speed
                self.jump_count -= 1
                
    def on_ground(self):
        if self.vel.y == 0:
            return True
        else:
            return False
            
    def detect_sqaut_down(self):
        if self.squat_down:
            return True
        else:
            return False
    
    def pos_change(self, platforms, platform_group):
        if self.moving_ret:
            self.acc.x += self.vel.x * FRIC
            self.vel += self.acc
            if self.detect_sqaut_down():
                self.vel.x = 0 
                self.acc.x = 0
            self.pos += self.vel + 0.5 * self.acc

    def border_detect_and_xpos_update(self, platforms, platform_group):
        if self.pos.x > 1500:
            self.pos.x = 1500
        if self.pos.x < 0:
            self.pos.x = 0
        self.rect.bottomleft = (self.pos.x, self.pos.y)
       
    def shield_following_and_invisible(self):
        if self.get_shield_ret == True:
            self.shield_image.rect.center = self.rect.center
        else:
            self.shield_image.rect.center = (-1000,-1000)
    def jump_down_platform(self,able_to_scroll):
        if(self.squat_down_cnt >= 2 and self.detect_hit(able_to_scroll)):
            self.go_down_ground_button = True
        else:
            self.go_down_ground_button = False
        
    def move_position(self):
        return self.pos

    def all_cnt_del(self):
        self.squat_down_cnt = 0

    def movement(self, platforms, platform_group,able_to_scroll,bullet_group):
    
        self.speed_change(platforms, platform_group)
        self.pos_change(platforms, platform_group)
        self.border_detect_and_xpos_update(platforms, platform_group)
        self.shield_following_and_invisible()
        self.disard_weapon()
        self.jump_down_platform(able_to_scroll)
        self.shoot(bullet_group)
        self.shield_broken(bullet_group)
        self.pos_update(platform_group)
        self.normal_attacking()
    

    def normal_attack_button(self):
        self.normal_attack_pre_ret = self.normal_attack_ret
        try:
            if self.key_event.button == 8 and  self.key_event.type == JOYBUTTONDOWN:
                self.normal_attack_ret = True
            elif self.key_event.button == 8 and  self.key_event.type == JOYBUTTONUP:
                self.normal_attack_ret = False
        except AttributeError:
            return
        # if self.keys[pygame.K_k]:
        #     self.normal_attack_ret = True
        # else:
        #     self.normal_attack_ret = False
    def moving_button(self):
        try:
            if self.key_event.value == (-1, 0):
                self.move_left_press = True
                self.move_right_press = False
                self.facing_right = False
            elif self.key_event.value == (0, 0):
                self.move_left_press = False
            if self.key_event.value == (1, 0):
                self.move_right_press = True
                self.move_left_press = False
                self.facing_right = True
            elif self.key_event.value == (0, 0):
                self.move_right_press = False
        except AttributeError:
            return
    def jumping_button(self):
        self.pre_space = self.jump_button
        try:
            if  self.key_event.button == 0 and self.key_event.type == JOYBUTTONDOWN:
                self.jump_button = True
            if self.key_event.button == 0 and self.key_event.type == JOYBUTTONUP:
                self.jump_button = False
        except AttributeError:
            return

        # if self.keys[pygame.K_SPACE]:
        #     self.jump_button = True
        # else:
        #     self.jump_button = False
    def squat_down_button(self):
        self.squat_down_pre = self.squat_down
        try:
            if self.key_event.value == (0,-1):
                self.squat_down = True
            elif self.key_event.value == (0,0):
                self.squat_down = False
            if self.key_event.value == (0,-1):
                self.squat_down_cnt+=1
        except AttributeError:
            return
        

    def shoot_botton(self):
        if self.get_weapon != None:
            try:
                if self.key_event.button == 8 and self.key_event.type == JOYBUTTONDOWN:
                    self.shooting_ret = True
                else:
                    self.shooting_ret = False
            except AttributeError:
                self.shooting_ret = False
    def keyboard_control(self,key_event):
        self.key_event = key_event
        self.jumping_button()
        self.squat_down_button()
        self.shoot_botton()
        self.moving_button()
        self.normal_attack_button()
    


                 