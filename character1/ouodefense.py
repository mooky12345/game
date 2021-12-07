import pygame
class ouodefense(pygame.sprite.Sprite):
    def __init__(self):
        self.surf = pygame.Surface([30,120]).convert_alpha()
        self.surf.fill((0,0,0,0))
        self.rect = self.surf.get_rect()
        self.rect.center = (-100,-100)
        self.cooldown = 500
    def implement(self,pos,dir):
        if self.cooldown == 0:
            if dir == 0:
                self.rect.bottomleft = (pos[0],pos[1])
            if dir == 180:
                self.rect.bottomleft = (pos[0]-30,pos[1])
    def out_width(self):
        self.rect.center = (-100,100)
    def reset_cooldown(self):
        self.cooldown = 500
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1