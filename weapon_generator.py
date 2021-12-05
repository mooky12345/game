import pygame
import random as rd

vec = pygame.math.Vector2
HEIGHT = 400
backgound_WIDTH = 700
class random_generation(pygame.sprite.Sprite):
    def __init__(self,transparency,R,G,B):
        super().__init__()
        self.chwid = 30
        self.chhie = 30 
        self.bullet_count = 5
        self.image_weapon = None
        self.weapon_image = {
            "shield" : 0,
            "gun" : 1
        }
        self.x_range = {
            "background":[105,800],
            "plat1" : [340,380],
            "plat2" : [98,194]
        }
        self.y_position =  {
            "background":110,
            "plat1" : 150,
            "plat2" : 240
        }
        self.image_type = []
        self.pos = vec(-1111,-1111)
        for im in self.weapon_image:
            self.image_type.append("weapon/{}.png".format(im))
        self.image = self.image_type[self.weapon_image[rd.choice(list(self.weapon_image))]]
        self.image_varible_setter()
        self.rect.left = -100
        self.rect.bottom = -100
        self.background_width = 900
        self.background_height = 400
        self.image_varible_setter()
        self.pos_updating()
    def image_varible_setter(self):
        charImage = pygame.image.load(self.image)
        charImage = pygame.transform.scale(charImage, (self.chwid,self.chhie))
        self.rect = charImage.get_rect()
        self.surf = pygame.Surface((self.rect.right, self.rect.bottom))
        self.surf.blit(charImage, ((0,0)))
    def image_detect_hit(play,group):
        pressed = pygame.key.get_pressed()
        hits = pygame.sprite.spritecollide(play,group,False)
        for item in hits:
            if play.get_weapon == None and item.image_weapon == "gun" and pressed[pygame.K_j]:
                item.pos_out_width()
                play.get_weapon = item
            elif item.image_weapon == "shield":
                play.get_shield_ret = True
                item.pos_out_width()
    def get_weapon(self):
        return self.image_weapon
    def pos_updating(self):
        self.rect.x,self.rect.y=self.pos.x,self.pos.y
    def pos_out_width(self):
        self.pos.x = -111
        self.pos.y = -111
        self.image_varible_setter()
        self.pos_updating()
    def generate(self):
        choose_x_range = self.x_range[rd.choice(list(self.y_position))]
        self.pos.x = rd.randint(choose_x_range[0],choose_x_range[1])
        self.pos.y = self.y_position[rd.choice(list(self.y_position))]
        chh = rd.choice(list(self.weapon_image))
        self.image = self.image_type[self.weapon_image[chh]]
        self.image_weapon = chh
       
        self.image_varible_setter()
        self.pos_updating()
    def redraw(self, change_x,change_y, original_x, original_y):
        self.bg_x = change_x
        self.bg_y = change_y

        if self.bg_y < 100:
            self.test_y = 100 - self.bg_y
        if self.bg_y >= 100: self.test_y = 0

        # if change_y<0:
        #    self.set_visible(False)
        # else :
        #     self.set_visible(True)
        # if change_x:  # X軸
        #     if self.bg_x < backgound_WIDTH / 2:
        #         self.rect.center = (original_x, HEIGHT - original_y + self.test_y)
        #     elif self.bg_x > backgound_WIDTH / 2 and self.bg_x < self.background_width - backgound_WIDTH / 2:
        #         self.rect.center = (original_x - (change_x - backgound_WIDTH / 2),
        #                             HEIGHT - original_y + self.test_y)
        #     elif self.bg_x > self.background_width - backgound_WIDTH / 2:
        #         self.rect.center = (original_x - (550 - backgound_WIDTH / 2), HEIGHT - original_y + self.test_y)