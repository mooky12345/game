import pygame
from pygame import image

class Role_icon (pygame.sprite.Sprite):
    def __init__(self,h=100,w=100,src="",name="",x=0,y=0,x_size=1,y_size=1):
        super().__init__()
        self.x_size=x_size
        self.y_size=y_size
        self.name=name
        self.h=h
        self.w=w
        self.src=src
        self.surf=pygame.Surface((self.h* self.x_size, self.w* self.y_size))
        self.rect=self.surf.get_rect()
        self.rect.bottomleft=(x,y)
        self.type_match={"cover":"select_screen/{}/cover.jpg".format(self.src),"uncover":"select_screen/{}/uncover.jpg".format(self.src)}
        self.image=""
        self.press=False
    def image_reset(self,type="uncover"):
        Image=pygame.image.load(self.type_match[type])
        self.image=pygame.transform.scale(Image,(self.h*self.x_size,self.w*self.y_size))
        # self.rect=self.image.get_rect()
    def set(self,type="uncover"):
        self.image_reset(type)
        self.surf.fill((0,0,0))
        self.surf.blit(self.image,(0,0))
    def mouse_over(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        return False
    def mouse_press(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.press=True
    
    def update(self):
        if self.mouse_over():
            self.set(type="cover")
        else: self.set(type="uncover")
    def change_size(self,x_size,y_size):
        self.surf=pygame.Surface((self.h* self.x_size, self.w* self.y_size))
        self.image_reset()
        self.surf.blit(self.image,(0,0))
        self.x_size=x_size
        self.y_size=y_size
