import pygame
import math
SCREEN_WIDTH = 1500
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction_degree):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.chwid = 20
        self.chhie = 10
        self.image = pygame.image.load("bullet/1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.chwid, self.chhie))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction_degree = direction_degree

    def update(self,player,bullet_group):
 
        self.rect.x += (self.speed * math.cos(math.radians(self.direction_degree)))
        self.rect.y -= (self.speed * math.sin(math.radians(self.direction_degree)))
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()

        if pygame.sprite.spritecollide(player, bullet_group, False):
            player.blood.cut_blood(10,1)
            self.kill()
            
               