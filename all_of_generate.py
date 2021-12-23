from weapon_generator import random_generation
import pygame as py

class all_generate():
    def __init__(self):
        self.generator_cnt = 0
        self.total = 12
        self.generator = [0]*self.total
        self.generator_guoup = py.sprite.Group()
    def declear(self):
        for i in range(self.total):
            self.generator[i] = random_generation()
        for i in range(self.total):
            self.generator_guoup.add(self.generator[i])
    def all__generate(self):
        if(self.generator_cnt == self.total):
            return 
        self.generator[self.generator_cnt].generate()
        self.generator_cnt+=1
    def update(self,play,platform,event):
        random_generation.image_detect_hit(play,self.generator_guoup,event)
        for item in self.generator:
            item.posy_updating(platform,self.generator_guoup)