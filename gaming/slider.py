import pygame as py
import sys
white=((255,255,255))
green=((0,255,0))
blue=((0,0,255))
WIDTH=700
class Slider():
        def __init__(self):
                self.surf=py.Surface((WIDTH,400))
                vec = py.math.Vector2
                self.pos=vec(200,100)
                self.slider_lengh=200
                self.slider_height=20

                self.circle_radias=30
                self.interval=self.slider_lengh/float(100)
                self.volume=50
                self.up=False
                self.down=False
                py.draw.circle(self.surf,white,(self.pos.x+self.interval*self.volume,self.pos.y+self.slider_height/2),self.circle_radias,0)
                py.draw.rect(self.surf,white,[self.pos.x,self.pos.y,self.slider_lengh,self.slider_height],0)
                self.circle_pos=vec(self.pos.x+self.interval*self.volume,self.pos.y+self.slider_height/2)
                self.font = py.font.Font('freesansbold.ttf', 32)
                self.text = self.font.render('Volume is ' +str( self.volume), True, green, blue)
                self.textRect = self.text.get_rect()
                self.textRect.topleft = (10, 10)
                self.surf.blit(self.text,self.textRect)
                self.t=0
        def get_volume(self):
            pass
        def on_slider(self,event_list):
            for event in event_list:
                if event.type==py.MOUSEBUTTONDOWN:
                    self.down=True
                    self.up=False
                if event.type==py.MOUSEBUTTONUP:
                    self.up=True
                    self.down=False
                if self.down:
                    (mouse_x,mouse_y)=py.mouse.get_pos()
                    if(mouse_x<=self.circle_pos.x+self.circle_radias and mouse_x>=self.circle_pos.x-self.circle_radias and mouse_y<= self.circle_pos.y+self.circle_radias and  mouse_y>= self.circle_pos.y-self.circle_radias):

                        return True
            return False
        def update(self,event_list):
            if  self.on_slider(event_list):
                  self.update_volume()
                  self.update_text()
                  self.redraw()
          
        def set_volume(self,Sound_name):
            Sound_name.set_volume(1.0*self.volume/100)
        
        def update_volume(self):
            if self.circle_pos.x < self.pos.x:
                self.volume = 0
            elif self.circle_pos.x > self.pos.x + self.slider_lengh:
                self.volume = 100
            else:
                (mouse_x,mouse_y)=py.mouse.get_pos()
                self.volume = int((mouse_x - self.pos.x) / float(self.interval))
                if self.volume<0:
                    self.volume=0
                elif self.volume>100:
                    self.volume=100
          
        def redraw(self):
            self.circle_pos.x=self.pos.x+self.volume*self.interval
            self.surf.fill((0,0,0))
            py.draw.circle(self.surf,white,(self.pos.x+self.interval*self.volume,self.pos.y+self.slider_height/2),self.circle_radias,0)
            py.draw.rect(self.surf,white,[self.pos.x,self.pos.y,self.slider_lengh,self.slider_height],0)
            self.surf.blit(self.text,self.textRect)
        def get_volume(self):
            return self.volume
        def update_text(self):
            self.text = self.font.render('Volume is ' + str(self.volume), True, green, blue)
        def set_event_lsit(self,event_list):
            self.event_list=event_list
        def get_event_list(self):
            return self.event_list