import pygame
SCREEN_WIDTH = 900
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.chwid = 20
        self.chhie = 10
        self.image = pygame.image.load("bullet/1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.chwid, self.chhie))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction = direction

    def update(self,player,bullet_group):
 
        self.rect.x += (self.direction * self.speed)

        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()

        if pygame.sprite.spritecollide(player, bullet_group, False):
            if player.get_shield_ret == True:
                player.shield_broken()
            
               