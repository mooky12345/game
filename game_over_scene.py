import pygame as py
class end_scene():
    def __init__(self,winner_image_src):
        self.wid = 300
        self.hie = 200
        
        self.backgrond_scene = py.image.load("end_scene/background.png")
        self.backgrond_scene = py.transform.scale(self.backgrond_scene,(1500,800)).convert_alpha()
        self.backgrond_scene_rect = self.backgrond_scene.get_rect()  
        self.crown = py.image.load("crown/crown.png")
        self.crown = py.transform.scale(self.crown,(50,150)).convert_alpha()
        self.crown_rect = self.crown.get_rect()
        self.winner_image = py.image.load(winner_image_src)
        self.winner_image = py.transform.scale(self.winner_image,(700,400)).convert_alpha()
        self.winner_image_rect =  self.winner_image.get_rect()
        self.crown_rect.center = (750,100)
        self.crown_rect.center = (750,200)
    def update(self):
        if self.crown_rect.centery < 210:
            self.crown_rect.centery += 1 
    def bliting(self,background):
        background.blit(self.backgrond_scene, self.backgrond_scene_rect)
        background.blit(self.crown,self.crown_rect)
        background.blit(self.winner_image,(500,200))
    # def set_winner(self,winner):
    #     pass