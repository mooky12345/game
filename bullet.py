import pygame
import math
SCREEN_WIDTH = 1500
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction_degree,toxic_ret):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.chwid = 15
        self.chhie = 15
        self.toxic_ret = toxic_ret
        if toxic_ret:
            self.image = pygame.image.load("bullet/2.png").convert_alpha()
        else:
            self.image = pygame.image.load("bullet/1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.chwid, self.chhie))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction_degree = direction_degree
        self.knock_back_range = 5
        self.toxic_statement = toxic_ret
    def update(self,players,bullet_group):
        self.rect.x += (self.speed * math.cos(math.radians(self.direction_degree)))
        self.rect.y -= (self.speed * math.sin(math.radians(self.direction_degree)))
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.top > 800 or self.rect.top < 0:
            self.kill()
        if pygame.sprite.spritecollide(self,players,False):
            hits = pygame.sprite.spritecollide(self,players,False)
            for item in hits:
                if self.toxic_statement:
                    players.toxic_statement = True
                if self.direction_degree < 270:
                    item.pos.x += self.knock_back_range*math.cos(math.radians(self.direction_degree))
                if self.direction_degree > 270:
                    item.pos.x += self.knock_back_range*math.cos(math.radians(self.direction_degree))
                item.blood.cut_blood(5,1)
            self.kill()
               