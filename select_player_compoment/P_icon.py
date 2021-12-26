import pygame
from select_player_compoment.role_icon import Role_icon

class Player_number_icon(Role_icon):
    def __init__(self, h=100, w=100, src="", name="", x=0, y=0, x_size=2, y_size=3,select="1"):
        super().__init__(h=h, w=w, src=src, name=name, x=x, y=y, x_size=x_size, y_size=y_size)
        self.image = pygame.image.load("player_number_icon/{}.png".format(select))
        self.image=pygame.transform.scale(self.image,(self.w*self.x_size,50))
        self.surf=pygame.Surface((self.w*self.x_size,50))
        self.surf.fill((0,0,0))
        self.surf.blit(self.image,(0,0))