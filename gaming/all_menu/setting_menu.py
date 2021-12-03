import pygame 
from button import Button
from slider import Slider 
class Setting_menu():
    def __init__(self):
      self.DOWN_key=False
      self.UP_key=False
      self.button_back=Button("back!", (280, 28),start_function)
      self.surf=pygame.Surface((450,400))
      self.Volume_slider=Slider()
    def check_event(self):
      self.DOWN_key=False
      self.UP_key=False
    def draw(self,event_list):
      buttons=[self.button_back]
      sliders=[self.Volume_slider]
      
      for slider in sliders:
        slider.update(event_list)
      self.surf.fill((0,0,0))
      for button in buttons:
        button.redraw()
      for slider in sliders:
        slider.redraw()
      for slider in sliders:
        self.surf.blit(slider.surf,(0,0))
      for button in buttons:
        self.surf.blit(button.surf,button.rect)
def start_function():
    print("back")
