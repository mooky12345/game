import pygame as py
from character import Character
from character import attack
class skill(Character,attack):
    
    def attack_mode_1(self, Character, attack):
        if Character.attack_mode[0]:
            if Character.facing_right:
                attack.vel.x = 5
                Character.vel = attack.vel

            else:
                attack.vel.x = -5
                Character.vel = attack.vel
            
    def attack_mode_2(self, Character, attack):
        if Character.attack_mode[1]:
            if Character.name == 'cats':
                if Character.facing_right:
                    pass
                else:
                    pass

                
    def attack_mode_3(self, Character, attack):
        if Character.attack_mode[2]:
            if Character.name == 'cats':   
                if Character.facing_right:
                    pass
                else:
                    pass

                
    def attackment(self, Character, attack):
        pass
        if max(Character.attack_mode):
            Character.in_attack = True
            attack.trigger = True
            attack.pos = Character.pos
            self.attack_mode_1(Character, attack)
            self.attack_mode_2(Character, attack)
            self.attack_mode_3(Character, attack)
        
    


