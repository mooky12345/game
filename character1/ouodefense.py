import pygame
class ouodefense(pygame.sprite.Sprite):
    def __init__(self):
        self.surf = pygame.Surface([30,120]).convert()
        self.surf.fill((0,0,0,100))
        self.rect = self.surf.get_rect()
        self.rect.center = (-100,-100)
        self.cooldown = 100
        self.direction = None
    def implement(self,pos):
        if self.cooldown == 0:
            
            if self.direction == 0:
                self.rect.bottomleft = (pos[0]+30,pos[1])
            if self.direction == 180:
                self.rect.bottomleft = (pos[0]-30,pos[1])
    def out_width(self):
        self.rect.center = (-100,-100)
    def reset_cooldown(self):
        self.cooldown = 100
    def update(self,dir,bullet):
        self.direction = dir
        hit = pygame.sprite.spritecollide(self, bullet, False)
        for item in hit:
            item.kill()
        self.cooldown_creasing()
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1