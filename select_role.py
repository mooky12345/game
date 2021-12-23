import pygame
from role_icon import Role_icon
from BG import WIDTH, background_test
from text import Text
Height=800
Width=1500
class cool():
    def __init__(self):
        player_1=Role_icon(src="kali",x=350,y=600,name="1",x_size=2,y_size=3)
        player_2=Role_icon(src="osa",x=800,y=600,name="2",x_size=2,y_size=3)
        player_3=Role_icon(src="clash",x=1250,y=600,name="3",x_size=2,y_size=3)
        self.surf=pygame.Surface((Width,Height))
        self.start=50
        self.gap=150
        self.all_player=[player_1,player_2,player_3]
        self.bg=background_test(image="background/3.jpg")
        self.surf.blit(self.bg.surf,(0,0))
        self.dx=0
        # self.place_role_image_pos()
    # def place_role_image_pos(self):
    #     pos=self.start
    #     cnt=0
    #     for entity in self.all_player:
    #         self.surf.blit(entity.surf,(pos+cnt*self.gap,600))
    #         cnt+=1
    def select_complete_animation(self,one,two):
            self.bg=background_test(image="background/vs.png")
            self.surf.fill((0,0,0))
            self.surf.blit(self.bg.surf,(0,0))
            self.surf.blit(one.surf,(1500-self.dx-two.w*two.x_size,400))
            self.surf.blit(two.surf,(self.dx,400))
            for i in self.all_player:
                i.update()
    def update(self):
        for i in self.all_player:
            i.update()
        for i in self.all_player:
            self.surf.blit(i.surf,i.rect)
        self.surf.blit(self.test.txt_surf,(Width/2,Height/10))
        # self.place_role_image_pos()
