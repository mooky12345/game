import pygame as py
class end_scene():
    def __init__(self,winner_image_src):
        self.wid = 300
        self.hie = 200
        
        self.backgrond_scene = py.image.load("end_scene/background.png")
        self.backgrond_scene = py.transform.scale(self.backgrond_scene,(1500,800)).convert_alpha()
        self.backgrond_scene_rect = self.backgrond_scene.get_rect()  
        self.crown = py.image.load("crown/crown.png")
        self.crown = py.transform.scale(self.crown,(500,400)).convert_alpha()
        self.crown_pos = [750,0]
        self.crown_rect = self.crown.get_rect()
        self.winner_image = py.image.load(winner_image_src)
        self.winner_image = py.transform.scale(self.winner_image,(700,400)).convert_alpha()
        self.winner_image_rect =  self.winner_image.get_rect()
        self.winner_image_rect.center = (752,400)
        self.crown_rect.center = (750,0)
    def update(self):
        if self.crown_pos[1] < 100:
            self.crown_pos[1] += 1
        self.crown_rect.center = self.crown_pos
    def bliting(self,background):
        background.blit(self.backgrond_scene, self.backgrond_scene_rect)
        background.blit(self.winner_image,self.winner_image_rect)
        background.blit(self.crown,self.crown_rect)
        