import pygame
from button import Button
class select_role_number_screen():
    def __init__(self):
        self.player_number=0
        self.surf=pygame.Surface((1500,800))
        self.surf.fill((128,128,128))
        self.button_01=Button("One", (280, 220))
        self.button_02 = Button("Two", (380, 220), bg=(50, 200, 20))
        self.button_03 = Button("Three", (480, 220), bg=(50, 200, 20))
        self.buttons=[self.button_01,self.button_02,self.button_03]
    def set_player_number(self,number):
        self.player_number=number
    def update(self):
        for button in self.buttons:
            button.redraw()
        for button in self.buttons:
            self.surf.blit(button.surf,button.rect)
# def print_123():
#     print("select_number_complete")