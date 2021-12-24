import pygame
from character import Character
from bullet import Bullet
class toxic():
    def __init__(self):
        self.cooldown = 300
        self.max_cooldown = 300
    def implement(self,bullet_group,own_group,dir,rect):
        if self.cooldown == 0:
            print(self.cooldown)
            self.cooldown = 300
            if dir == 0:
                bullet = Bullet(rect.centerx + 50,rect.centery-5, dir,True)
            if dir == 180:
                bullet = Bullet(rect.centerx - 50,rect.centery-5, dir,True)
            bullet_group.add(bullet)
            own_group.add(bullet)
    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1
