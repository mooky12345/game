from character import Character
from missile import missile
import pygame
class player3(Character):
    def __init__(self, name, cx, cy, image_path):
        super().__init__(name, cx, cy, image_path)
        self.missile_ret = False
        self.missile_pre_ret = False
        self.shoting_missile = missile()
    def shooting_follow(self):
        pass
    def shooting_missile(self):
        if self.missile_ret and not self.missile_pre_ret:
            self.shoting_missile.implement()
        self.shoting_missile.update()
    def key_get(self):
        self.missile_pre_ret = self.missile_ret
        if self.keys[pygame.K_y]:
            self.missile_ret = True
        else:
            self.missile_ret = False