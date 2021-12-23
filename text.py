import pygame

class Text():
    def __init__(self,font_name="Segoe Print", font_size=70,txt="select roles",x=0,y=0):
        self.txt = txt
        self.font=pygame.font.SysFont(font_name,font_size)
        self.fg=(0,255,0)
        self.txt_surf = self.font.render(self.txt, True, (self.fg))
        self.txt_rect = self.txt_surf.get_rect(bottomleft=(x,y))
    