import pygame

class explosion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = 10
        self.surf = pygame.Surface([self.size,self.size]).convert()
        self.images=[]
        for i in range(1,25):
            image = pygame.image.load("explosion_animation/{}.png".format(i)).convert_alpha()
            self.images.append(image)
        self.surf.fill((0,255,0,100))
        self.rect = self.surf.get_rect()
        self.rect.center = (-100,-100)
        self.cooldown = 100
        self.direction = None
        self.exist = False 
        self.littlefire_group = pygame.sprite.Group()
        self.pos = None
    def implement(self,pos,dir):
        if dir == 0:
            self.pos = pos
        if dir == 180:
            self.pos = pos
        self.exist = True
    def out_width(self):
        self.rect.center = (-100,-100)
    def reset_cooldown(self):
        self.cooldown = 100
    def width_changing(self):
        self.size += 2
        if self.size>95:
            pass
        else:
            self.image_cnt=int(self.size/4+1)
        #self.surf = pygame.Surface([self.size,self.size]).convert()
        self.surf = pygame.transform.scale(self.images[self.image_cnt-1],(self.size,self.size)).convert_alpha()
        self.rect = self.surf.get_rect()
        self.rect.center = self.pos
    def update(self,players):
        if self.exist:
            self.width_changing()
            if pygame.sprite.spritecollide(self,players,False):
                hits=pygame.sprite.spritecollide(self,players,False)
                for player in hits:
                    player.knock_back(self.rect.center,6,40)
                    player.blood.cut_blood(15,True)
        if self.size > 100:
            self.size = 20
            self.surf = pygame.Surface([self.size,self.size]).convert()
            self.rect = self.surf.get_rect()
            self.out_width()
            self.exist = False
        self.cooldown_creasing()
    def cooldown_creasing(self):
        if self.cooldown > 0:
            self.cooldown -=1