import pygame
class transport_damage(pygame.sprite.Sprite):
    def __init__(self):
        self.surf1 = pygame.Surface([30,60]).convert()
        self.surf1.fill((0,0,0,100))
        self.rect1 = self.surf1.get_rect()
        self.rect1.center = (-100,-100)
        self.surf2 = pygame.Surface([30,60]).convert()
        self.surf2.fill((0,0,0,100))
        self.rect2 = self.surf2.get_rect()
        self.rect2.center = (-100,-100)
        self.exist = False
        self.speed = 10
        self.cooldown = 100
        self.max_cooldown=100
    def implement(self,pos,player):
        self.exist = True
        if self.cooldown == 0:
            self.cooldown = 100 
            self.rect1.bottomleft = (pos[0]+30,pos[1])
            self.rect2.bottomright = (pos[0],pos[1])
            self.transport(player)
    def transport(self,player):
        player.pos[1] -= 200
    def update(self):
        self.cooldown_creasing()
        if self.exist:
            self.rect1.left += self.speed
            self.rect2.right -= self.speed
            if self.rect1.left > 1500 or self.rect2.right < 0:
                self.exist = False
                self.rect1.center = (-100,-100)
                self.rect2.center = (-100,-100)
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1
