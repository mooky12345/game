import pygame
from character import HEIGHT
class test_plat(pygame.sprite.Sprite):
    def __init__(self, length, height, R, G, B, transparency, x=0, y=0,cnt=0,v=1,dir=1):
         super().__init__()
         self.x = x
         self.y = y
         self.R=R
         self.G=G
         self.B=B
         self.dir=dir
         self.v=v
         self.origin_cnt=cnt
         self.cnt=0
         self.cnt_max=cnt
         self.image = pygame.Surface((length, height)).convert_alpha()
         self.image.fill((R, G, B, transparency))
         self.background_width = 900
         self.background_height = 900
         self.rect = self.image.get_rect(bottomleft=(x,y))
         self.test_y=0
         self.visible=0
    def plat_redraw(self, change_x,change_y, original_x, original_y):
        self.refresh()
        self.bg_x = change_x
        self.bg_y = change_y

        # if self.bg_y < 100:
        #     self.test_y = 100 - self.bg_y
        # if self.bg_y >= 100: self.test_y = 0

        # if change_y<0:
        #    self.set_visible(False)
        # else :
        #     self.set_visible(True)
        
        # if change_x:   # X軸
        #     if self.bg_x < backgound_WIDTH / 2:
        #         self.rect.center = (original_x, HEIGHT - original_y+self.test_y+self.cnt)
        #     elif self.bg_x > backgound_WIDTH / 2 and self.bg_x < self.background_width - backgound_WIDTH / 2:
        #         self.rect.center = (original_x - (change_x - backgound_WIDTH / 2),
        #                             HEIGHT - original_y+self.test_y+self.cnt)
        #     elif self.bg_x > self.background_width - backgound_WIDTH / 2:
        #         self.rect.center = (original_x-(550-backgound_WIDTH / 2), HEIGHT - original_y+self.test_y+self.cnt)
        if self.dir==1:
            self.rect.center = (original_x, -(HEIGHT - original_y+self.test_y+self.cnt))
        if self.dir==2:
            self.rect.center=(original_x+self.cnt, -(HEIGHT - original_y+self.test_y))
    def set_visible(self,bool):
        self.visible=bool
        if not(self.visible):
            self.image.fill((self.R, self.G, self.B, 0))
        else : self.image.fill((self.R, self.G, self.B, 50))
    def refresh(self):
        if self.cnt<self.cnt_max:
            self.cnt+=self.v
        else:
            self.cnt_max=0
        if self.cnt>self.cnt_max:
            self.cnt-=self.v
        else:
            self.cnt_max=self.origin_cnt
    def set_v(self,v):
        self.v=v
    def set_dir(self,dir):
        self.dir=dir