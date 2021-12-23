import pygame, sys
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
class Button():
    def __init__(self, txt, location, bg=WHITE, fg=BLACK, size=(80, 30), font_name="Segoe Print", font_size=16):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size
        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])
        self.surf = pygame.surface.Surface(size)
        self.rect = self.surf.get_rect(center=location)
        self.surf.fill(self.bg)
        self.surf.blit(self.txt_surf, self.txt_rect)
        self.press=False
    def redraw(self):
        self.mouseover()
        self.surf.fill(self.bg)
        self.surf.blit(self.txt_surf, self.txt_rect)
 
    def mouseover(self):
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = GREY

    def mousebuttondown(self):
      pos = pygame.mouse.get_pos()
      if self.rect.collidepoint(pos):
        self.press=True
    def change(self,text):
        self.txt = text
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s // 2 for s in self.size])
        self.surf.fill(self.bg)
        self.surf.blit(self.txt_surf, self.txt_rect)
