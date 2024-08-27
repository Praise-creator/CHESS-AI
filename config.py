import pygame
import os
from sound import Sound
from theme import Theme

class Config: 
    
    def __init__(self):
        self.themes = []
        self.add_themes()
        self.idx = 0
        self.theme = self.themes[self.idx]
        #font
        self.move_sound = Sound(
            os.path.join('assets/sounds/move.wav')
        )
        self.capture_sound = Sound(
            os.path.join('assets/sounds/capture.wav')
        )
    
    
    def change_theme(self):
        self.idx += 1
        self.idx %= len(self.themes)
        self.theme = self.themes[self.idx]
    
    def add_themes(self):
        green = Theme()
        brown = Theme()
        blue = Theme()
        grey = Theme()
        
        self.themes = [green, brown, blue, grey]