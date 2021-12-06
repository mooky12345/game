import pygame as py
class music():
    def __init__(self):
        py.mixer.init()
        self.main_sound=py.mixer.Sound("music/123.wav")
        self.effect = py.mixer.Sound("music/123.mp3")
        self.effect.play()
        self.main_sound.play(-1)
    def play_music(self):
        py.mixer.Sound.play(self.main_sound)