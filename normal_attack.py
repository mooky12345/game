from genericpath import exists
import pygame
class normal_attack(pygame.sprite.Sprite):
    def __init__(self):
        self.surf = pygame.Surface([120,30]).convert()
        self.surf.fill((0,0,0,100))
        self.rect = self.surf.get_rect()
        self.rect.center = (-100,-100)
        self.direction = None
        self.exist = False
        self.speed = 10
        self.cooldown = 100
        self.exist_cooldown = 13
    def implement(self,dir,pos):
        self.direction = dir
        self.exist = True
        if self.direction == 0:
            self.rect.left = pos[0]+30
            self.rect.top = pos[1]
        if self.direction == 180:
            self.rect.right = pos[0]
            self.rect.top = pos[1]
    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        if self.exist:
            self.exist_cooldown -= 1
            if self.exist_cooldown < 0:
                self.exist_cooldown = 13
                self.exist = False
                self.rect.center = (-100,-100)
