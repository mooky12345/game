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
        self.cooldown = 10
        self.skill_cooldown = 60
    def implement(self,dir,pos):
        if self.skill_cooldown == 0:
            self.skill_cooldown = 60
            self.direction = dir
            self.exist = True
            if self.direction == 0:
                self.rect.left = pos[0]+30
                self.rect.top = pos[1]-60
            if self.direction == 180:
                self.rect.right = pos[0]
                self.rect.top = pos[1]-69
    def update(self):
        if self.exist:
            self.cooldown_creaing()
            if self.cooldown == 0:
                self.exist = False
                self.cooldown = 10
                self.rect.center = (-100,-100)
        self.skill_cooldown_creaing()
    def cooldown_creaing(self):
        if self.cooldown > 0:
            self.cooldown -= 1
         
    def skill_cooldown_creaing(self):
        if self.skill_cooldown > 0:
            self.skill_cooldown -= 1
