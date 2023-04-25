import pygame
import constant as c
from star import Star
import random

class BG(pygame.sprite.Sprite):
    def __init__(self):
        super(BG, self).__init__()
        self.image = pygame.Surface(c.DISPLAY_SIZE)
        self.color = (8, 5, 20)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.stars = pygame.sprite.Group() # inisialisasi dengan sprite group kosong
        self.timer = random.randrange(1, 10)
        
    def update(self):
        self.stars.update()
        if self.timer == 0:
            new_star = Star() # perhatikan perubahan tanda "=" menjadi "==" 
            self.stars.add(new_star)
            self.timer = random.randrange(1, 10)
        self.image.fill(self.color)
        self.stars.draw(self.image)
        self.timer -= 1
