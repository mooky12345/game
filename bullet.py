import pygame
import math
SCREEN_WIDTH = 1500
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction_degree,toxic_ret):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.chwid = 20
        self.chhie = 10
        if toxic_ret:
            self.image = pygame.image.load("bullet/1.png").convert()
        else:
            self.image = pygame.image.load("bullet/1.png").convert()
        self.image = pygame.transform.scale(self.image, (self.chwid, self.chhie))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction_degree = direction_degree
        self.knock_back_range = 5
        self.toxic_statement = toxic_ret
    def update(self,player,bullet_group):
        
        self.rect.x += (self.speed * math.cos(math.radians(self.direction_degree)))
        self.rect.y -= (self.speed * math.sin(math.radians(self.direction_degree)))
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()

        if pygame.sprite.spritecollide(player, bullet_group, False):
            hits = pygame.sprite.spritecollide(player, bullet_group, False)
            for i in hits:
                if i.toxic_statement:
                    player.toxic_
            if self.direction_degree < 270:
                player.pos.x += self.knock_back_range*math.cos(math.radians(self.direction_degree))
            if self.direction_degree > 270:
                player.pos.x += self.knock_back_range*math.cos(math.radians(self.direction_degree))

            player.blood.cut_blood(5,1)
            self.kill()
               