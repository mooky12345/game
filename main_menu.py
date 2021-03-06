import pygame 
from button import Button
WIDTH=1500
class main_Menu():
    def __init__(self,start,two,Fantastic,Guide,Setting):
        self.button_01 = Button("{}".format(start), (WIDTH/2, 180))
        self.button_02 = Button("{}".format(two), (WIDTH/2, 220),  bg=(50, 200, 20))
        self.button_03 = Button("{}".format(Fantastic), (WIDTH/2, 260),  bg=(50, 200, 20))
        self.button_04 = Button("{}".format(Guide), (WIDTH/2, 300),  bg=(50, 200, 20))
        self.button_05 = Button("{}".format(Setting), (WIDTH/2, 340), bg=(50, 200, 20))
        self.buttons = {
            'first': self.button_01,
            'second': self.button_02,
            'third': self.button_03,
            'forth': self.button_04,
            'fifth':self.button_05
        }
    def draw(self):
        self.surf = pygame.Surface((WIDTH,800))
        self.surf.fill((0,0,0))
        for key in self.buttons:
          self.buttons[key].redraw()
        for key in self.buttons:
          self.surf.blit(self.buttons[key].surf,self.buttons[key].rect)
    def change_text(self,option,text):
        self.buttons["{}".format(option)].change(text)

