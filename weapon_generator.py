import pygame
import random as rd

from pygame.constants import JOYBUTTONDOWN
vec = pygame.math.Vector2
HEIGHT = 400
backgound_WIDTH = 700
class random_generation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.chwid = 30
        self.chhie = 30 
        self.count = 10
        self.image_weapon = None
        self.weapon_image = {
            "shield" : 0,
            "gun" : 1,
            "sword" : 2
        }
        self.x_range = {
            "background": [150,1320],
            "plat1" : [150,1320],
            "plat2" : [150,1320]
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
        charImage = pygame.image.load(self.image)
        charImage = pygame.transform.scale(charImage, (self.chwid,self.chhie))
        self.rect = charImage.get_rect()
        self.surf = pygame.Surface((self.rect.right, self.rect.bottom))
        self.surf.blit(charImage, ((0,0)))
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
    def image_detect_hit(play,group,event):
        pressed = pygame.key.get_pressed()
        hits = pygame.sprite.spritecollide(play,group,False)
        try:
            for item in hits:
                if  item.image_weapon != "shield" and event.button == 4 and event.type == JOYBUTTONDOWN:
                    item.pos_out_width()
                    play.get_weapon = item
                elif item.image_weapon == "shield":
                    play.get_shield_ret = True
                    item.pos_out_width()
        except AttributeError:
            return
    def posy_updating(self,platform_gruop,weapon_gruop):
        if len(pygame.sprite.spritecollide(self,weapon_gruop,False))>1:
            return
        if not pygame.sprite.spritecollide(self,platform_gruop,False):
            self.rect.bottom += 3
        else:
            for hit in pygame.sprite.spritecollide(self,platform_gruop,False):
                if hit.rect.top < self.rect.top:
                    self.rect.bottom += 3
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