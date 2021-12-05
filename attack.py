import pygame
from character import FRIC 


vec = pygame.math.Vector2

class attack(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos = vec(0, 0)
        self.trigger = False
        self.surf = pygame.Surface((0, 0))
        self.surf = self.surf.convert_alpha()
        self.surf.fill((0, 0, 0, 0))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
    def movement(self):
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        if self.detect_sqaut_down():
            self.vel.x = 0 
            self.acc.x = 0
        self.pos += self.vel + 0.5 * self.acc 
        
