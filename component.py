import pygame
import pygame.gfxdraw
from PIL import Image, ImageDraw

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
GREY  = (128, 128, 128)
PI = 3.1415
class circle():
    def __init__(self,transparency=50) :
        self.pil_size = 30
        self.pil_image = Image.new("RGBA", (self.pil_size, self.pil_size))
        self.pil_draw = ImageDraw.Draw(self.pil_image)
        #pil_draw.arc((0, 0, pil_size-1, pil_size-1), 0, 270, fill=RED)
        # self.pil_draw.pieslice((0, 0, self.pil_size-1, self.pil_size-1), 90, 0, fill=(0,0,   0,transparency))
        self.transparency=transparency
        mode = self.pil_image.mode
        size = self.pil_image.size
        data = self.pil_image.tobytes()
        self.image = pygame.image.fromstring(data, size, mode)
        self.surf=pygame.Surface((30,30)).convert_alpha()
        self.surf.fill((0,0,0,0))
    def update(self,surf,arc=-90,x=0,y=0):
        self.pil_draw.pieslice((0, 0, self.pil_size-1, self.pil_size-1), 270, arc, fill=(0,0,0,100))
        mode = self.pil_image.mode
        size = self.pil_image.size
        data = self.pil_image.tobytes()
        self.image = pygame.image.fromstring(data, size, mode)
        surf.blit(self.image,(x,y))