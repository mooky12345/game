import pygame as py
class stage_select():
    def __init__(self):
        self.wid = 300
        self.hie = 200
        self.stage1_image = py.image.load("background/1.jpg")
        self.stage2_image = py.image.load("background/2.jpg")
        self.stage3_image = py.image.load("background/4.jpg")
        self.stage1_image = py.transform.scale(self.stage1_image,(self.wid, self.hie))
        self.stage2_image = py.transform.scale(self.stage2_image,(self.wid, self.hie))
        self.stage3_image = py.transform.scale(self.stage3_image,(self.wid, self.hie))
        self.stage1_rect = self.stage1_image.get_rect()
        self.stage2_rect = self.stage1_image.get_rect()
        self.stage3_rect = self.stage1_image.get_rect()
        self.rect_set = [self.stage1_rect,self.stage2_rect,self.stage3_rect]
        self.pos_update()
    def pos_update(self):
        self.stage1_rect.center = (375,400)
        self.stage2_rect.center = (750,400)
        self.stage3_rect.center = (1125,400)
    def update(self,event_list,background,stage_list): 
        pos = py.mouse.get_pos()
        for rect in self.rect_set:
            if rect.collidepoint(pos):
                self.bliting_frame(background,rect)
            else: 
                pass
        for event in event_list:
            if event.type == py.MOUSEBUTTONDOWN:
                for i in range(3):
                    if self.rect_set[i].collidepoint(pos):
                        stage_list[i] = True
        self.bliting(background)
    def bliting_frame(self,background,stage_rect):
        white_frame = py.Surface([self.wid+10,self.hie+10])
        own_rect = white_frame.get_rect()
        own_rect.center = stage_rect.center
        background.blit(white_frame,own_rect)
    def bliting(self,background):
        background.blit(self.stage1_image,self.stage1_rect)
        background.blit(self.stage2_image,self.stage2_rect)
        background.blit(self.stage3_image,self.stage3_rect)


