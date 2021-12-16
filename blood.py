import pygame, sys
class bloodline():
        def __init__(self):
            self.blood = 120
            self.Image = self.image = pygame.image.load("blood_image/1.png")
            self.Image = pygame.transform.scale(self.Image, (20, 20))
            self.Image2 = self.image = pygame.image.load("blood_image/2.png")
            self.Image2 = pygame.transform.scale(self.Image2, (20, 20))
            self.list = []
            self.rect = self.Image.get_rect()
            self.surf = pygame.Surface((150, 20))
            self.surf = self.surf.convert_alpha()
            self.surf.fill((100, 0, 0, 100))
            for i in range(0, 5, 1):
                self.list.append(self.Image)

        def set_blood(self, value):
            self.blood = value

        def cut_blood(self, value, out):
            if out:
                if self.blood - value < 0:
                    self.blood = 0
                else:
                    self.blood -= value

        def update(self):
            self.surf.fill((0, 0, 0, 0))
            many = int(self.blood / 20)
            for i in range(many, 5, 1):
                self.list[i] = self.Image2
            for i in range(0, 5, 1):
                self.surf.blit(self.list[i], (i * 30, 0))









