from weapon_generator import random_generation
import pygame as py

class all_generate():
    def __init__(self):
        self.generator_cnt = 0
        self.generator = [0]*5
        self.generator_guoup = py.sprite.Group()
    def declear(self):
       
        self.generator[0] = random_generation(23,23,23,23)
        self.generator[1] = random_generation(23,23,23,23)
        self.generator[2] = random_generation(23,23,23,23)
        self.generator[3] = random_generation(23,23,23,23)
        self.generator[4] = random_generation(23,23,23,23)

        for i in range(5):
            self.generator_guoup.add(self.generator[i])
    def all__generate(self):
        if(self.generator_cnt == 5):
            return 
        self.generator[self.generator_cnt].generate()
        self.generator_cnt+=1
    def detect_hits(self,play):
        random_generation.image_detect_hit(play,self.generator_guoup)
            