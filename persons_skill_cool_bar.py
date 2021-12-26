import pygame, sys,os
from component import circle
class cool_bar():
    def __init__(self,item_w=20,item_h=20,src=""):
        self.src="skill_icon/{}".format(src)
        self.surf=pygame.Surface((150,30)).convert_alpha()
        self.src_list=[]
        self.images=[]
        self.circles=[]
        self.item_number= len(os.listdir(self.src))
        for i in range(1, self.item_number + 1):
            img =self.src+"/{}.png".format(i)
            self.src_list.append(img)
    
        for src in self.src_list:
            Image = self.image = pygame.image.load(src)
            Image = pygame.transform.scale(Image, (item_w,item_h))
            self.images.append(Image)
        
        for i in range(1, self.item_number + 1):
            circle_1 =circle()
            self.circles.append(circle_1)

        for i in range(0, self.item_number, 1):
            self.surf.blit(self.images[i], (float(150/self.item_number*i), 0))
        self.x=0
    def update(self,arc=-90,arc2=-90,arc3=-90):
        self.surf.fill((0, 0, 0, 0))
        for i in range(0, self.item_number, 1):
            self.surf.blit(self.images[i], (float(150/self.item_number*i), 0))
        # for i in self.circles:
        #     i.update(self.surf,arc=self.x)
        # for i in range(0, self.item_number, 1):
            # self.surf.blit(self.circles[i].surf, (float(150/self.item_number*i)-10, 8))
        self.circles[0].update(self.surf,arc=arc,x=float(150/self.item_number*0)-5,y=0)
        self.circles[1].update(self.surf,arc=arc2,x=float(150/self.item_number*1)-5,y=0)
        if arc>=265:
            self.circles[0]=circle()
        if arc2>=265:
            self.circles[1]=circle()
        if arc3>=265:
            self.circles[2]=circle()









