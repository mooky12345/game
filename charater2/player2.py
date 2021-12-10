from character import Character
class player2(Character):
    def __init__(self, name, cx, cy, image_path):
        super().__init__(name, cx, cy, image_path)
        self.shooting_fireball_ret = False
        self.transporting_damage_ret = False
        self.shooting_fireball__pre_ret = False
        self.transporting_damage__pre_ret = False
    def shooting_fireball(self):
        pass
    def transporting_damage(self):

    def key_get(self):
        self.shooting_fireball_pre_ret = 
        if self.keys[pygame.K_y]:
            self.shooting_fireball_ret = True
        else:
            self.shooting_fireball_ret = False
        if self.keys[pygame.K_u]:
            self.ouohand_ret = True
        else:
            self.ouohand_ret = False
        if self.keys[pygame.K_i]:
            self.ouofoot_ret = True
        else:
            self.ouofoot_ret = False