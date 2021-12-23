import pygame
from button import Button
class pause_screen():
    def __init__(self):
       self.surf=pygame.Surface((1500,800))
       self.button_1=Button("restart", (225, 180))
       self.button_2=Button("back", (180, 250))
       self.button_3=Button("setting", (270, 250))
       self.buttons=[self.button_1,self.button_2,self.button_3]
    def update(self):
        for button in self.buttons:
            button.redraw()
        for button in self.buttons:
            self.surf.blit(button.surf,button.rect)