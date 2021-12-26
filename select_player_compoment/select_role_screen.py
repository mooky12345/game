import pygame
from select_player_compoment.role_icon import Role_icon
from select_player_compoment.P_icon import Player_number_icon
from BG import WIDTH, background_test
from text import Text
import math
Height=800
Width=1500
class role_screen():
    def __init__(self):
        player_1=Role_icon(src="kali",x=350,y=600,name="1",x_size=2,y_size=3)
        player_2=Role_icon(src="osa",x=800,y=600,name="2",x_size=2,y_size=3)
        player_3= Role_icon(src="clash",x=1250,y=600,name="3",x_size=2,y_size=3)
        self.test= Text()
        self.surf=pygame.Surface((Width,Height))
        self.start=50
        self.gap=150
        self.all_player=[player_1,player_2,player_3]
        self.bg=background_test(image="background/3.jpg")
        self.surf.blit(self.bg.surf,(0,0))
        self.dx=0
        self.dy=0
        self.test_1=Player_number_icon()
        self.test_2=Player_number_icon(select="2")
        self.test_3=Player_number_icon(select="3")

        # self.place_role_image_pos()
    # def place_role_image_pos(self):
    #     pos=self.start
    #     cnt=0
    #     for entity in self.all_player:
    #         self.surf.blit(entity.surf,(pos+cnt*self.gap,600))
    #         cnt+=1
    def select_complete_animation(self,list,player_cnt):
            self.bg=background_test(image="background/vs.png")
            self.surf.fill((0,0,0))
            self.surf.blit(self.bg.surf,(0,0))
            if player_cnt==2:
                self.surf.blit(list[0].surf,(1500-self.dx-list[0].w*list[0].x_size,400))
                self.surf.blit(self.test_1.surf,(1500-self.dx-list[1].w*list[1].x_size,400))
                self.surf.blit(list[1].surf,(self.dx,400))
                self.surf.blit(self.test_2.surf,(self.dx,400))
            else:
                self.surf.blit(list[0].surf,(1500-self.dx-list[0].w*list[0].x_size,400))
                self.surf.blit(self.test_1.surf,(1500-self.dx-list[1].w*list[1].x_size,400))
                self.surf.blit(list[1].surf,(self.dx,400))
                self.surf.blit(self.test_2.surf,(self.dx,400))
                self.surf.blit(list[2].surf,(Width/2,self.dy))
                self.surf.blit(self.test_3.surf,(Width/2,self.dy))
            for i in self.all_player:
                i.update()
    def update(self):
        for i in self.all_player:
            i.update()
        for i in self.all_player:
            self.surf.blit(i.surf,i.rect)
        self.surf.blit(self.test.txt_surf,(Width/2,Height/10))
    def re_init(self):
        player_1=Role_icon(src="kali",x=350,y=600,name="1",x_size=2,y_size=3)
        player_2=Role_icon(src="osa",x=800,y=600,name="2",x_size=2,y_size=3)
        player_3= Role_icon(src="clash",x=1250,y=600,name="3",x_size=2,y_size=3)
        self.test= Text()
        self.surf=pygame.Surface((Width,Height))
        self.start=50
        self.gap=150
        self.all_player=[player_1,player_2,player_3]
        self.bg=background_test(image="background/3.jpg")
        self.surf.blit(self.bg.surf,(0,0))
        self.dx=0
        self.dy=0
        self.test_1=Player_number_icon()
        self.test_2=Player_number_icon(select="2")
        self.test_3=Player_number_icon(select="3")