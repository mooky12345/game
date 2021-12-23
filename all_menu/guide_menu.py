import pygame 
from button import Button 
class guide_Menu():
    def __init__(self):
      self.DOWN_key=False
      self.UP_key=False
      self.button_01=Button("start!", (225, 180))
      self.button_02 = Button("Fantastic!", (225, 220), bg=(50, 200, 20))
      self.button_03 = Button("guild", (225, 260), bg=(50, 200, 20))
    def check_event(self):
      self.DOWN_key=False
      self.UP_key=False
    def draw(self):
      buttons=[self.button_01,self.button_02,self.button_03]
      self.surf = pygame.Surface((450,400))
      self.surf.fill((0,0,0))
      for button in buttons:
        button.draw()
      for button in buttons:
        self.surf.blit(button.surf,button.rect)
def start_function():
    print("Game start!")
 
 
def my_fantastic_function():
    print("按尛還沒做好 ")