import pygame
from genericpath import isfile
from pathlib import Path
import os
from pygame.locals import *
from blood import bloodline
from bullet import Bullet
from shield import *
from normal_attack import normal_attack
vec = pygame.math.Vector2
HEIGHT = 400
backgound_WIDTH = 900
ACC = 0.5
FRIC = -0.12
jump_speed = -13


class Character(pygame.sprite.Sprite):
    def __init__(self, name, cx, cy, image_path):
        super().__init__()
        self.normal_attack_ret = False
        self.normal_attack_pre_ret = False
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
        self.pre_space = 0
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
    def shoot(self,bullet_group):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        if self.get_weapon != None and self.get_weapon.image_weapon == "gun":
            if self.shoot_cooldown == 0 and self.get_weapon.count  > 0 and self.shooting_ret:
                self.shoot_cooldown = 20
                
                bullet = Bullet(self.rect.centerx + (self.rect.size[0] / 2 * math.cos(math.degrees(self.direction))),self.rect.centery-5, self.direction)
                bullet_group.add(bullet)
                self.own_bullet_group.add(bullet)
                self.get_weapon.count -= 1
    def normal_attacking(self):
        if self.normal_attack_ret and not self.normal_attack_pre_ret:
            if self.get_weapon.image_weapon == "sword" and  self.get_weapon.count > 0:
                self.normal_attack_image.implement(self.direction,self.pos)
            else:
                self.normal_attack_image.rect.center = (-100,-100)
    def disard_weapon(self):
        if self.get_weapon != None:
            if self.keys[pygame.K_h] :
                if self.get_weapon.count != 0:
                    self.get_weapon.rect.x,self.get_weapon.rect.y = self.pos.x,self.pos.y
                    self.get_weapon = None
                else:
                    self.get_weapon = None
    def shield_broken(self,bullet):
        if self.get_shield_ret == True:
            if pygame.sprite.spritecollide(self.shield_image, bullet, False):
                if not pygame.sprite.spritecollide(self.shield_image, self.own_bullet_group, False):
                    hit = pygame.sprite.spritecollide(self.shield_image, bullet, False)
                    hit[0].kill()
                    self.get_shield_ret = False
    def pos_update(self, plat):
        if self.get_weapon != None:
            print(self.get_weapon.pos.x,self.get_weapon.pos.y)
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

    def movement(self, platforms, platform_group,able_to_scroll,bullet_group):
        self.keyboard_control(platforms)
        self.speed_change(platforms, platform_group)
        self.pos_change(platforms, platform_group)
        self.border_detect_and_xpos_update(platforms, platform_group)
        self.shield_following_and_invisible()
        self.jump_down_platform(able_to_scroll)
        self.shoot(bullet_group)
        self.shield_broken(bullet_group)
        self.pos_update(platform_group)
        
    def keyboard_control(self, platforms):
        self.downcatch_button()
        self.jumping_button()
        self.squat_down_button()
        self.shoot_botton()
        self.moving_button()
        self.normal_attack_button

    def normal_attack_button(self):
        if self.keys[pygame.K_k]:
            self.normal_attack_ret = True
        else:
            self.normal_attack_ret = False
    def moving_button(self):

        if self.keys[pygame.K_LEFT]:
            self.move_left_press = True
            self.move_right_press = False
            self.facing_right = False
        else:
            self.move_left_press = False
        if self.keys[pygame.K_RIGHT]:
            self.move_right_press = True
            self.move_left_press = False
            self.facing_right = True
        else:
            self.move_right_press = False
        if self.keys[pygame.K_LEFT] and self.keys[pygame.K_RIGHT]:
            self.move_left_press = False
            self.move_right_press = False

    def downcatch_button(self):
        if self.keys[pygame.K_d] and self.keys[pygame.K_RIGHT]:
            self.downcatch_right = True
        if self.keys[pygame.K_d] and self.keys[pygame.K_LEFT]:            
            self.downcatch_left = True

    def jumping_button(self):
        if not self.pre_space and self.keys[pygame.K_SPACE]:
            self.jump_button = True
        else:
            self.jump_button = False
        self.pre_space = self.keys[pygame.K_SPACE]
        
    def squat_down_button(self):
        if self.keys[pygame.K_DOWN]:
            self.squat_down = True
        else:
            self.squat_down = False
        if not self.squat_down_pre and self.squat_down:
            self.squat_down_cnt+=1
        self.squat_down_pre = self.squat_down

    def shoot_botton(self):
        if self.get_weapon != None:
            if self.keys[pygame.K_k] and self.pre_shooting_ret == False and self.get_weapon.image_weapon == "gun":
                self.shooting_ret = True
            else:
                self.shooting_ret = False
        self.pre_shooting_ret = self.keys[pygame.K_k]
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
       
        if self.jump_button:
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


