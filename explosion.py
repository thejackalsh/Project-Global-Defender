import pygame
import constant as c
import random


class Explosion(pygame.sprite.Sprite):
    def __init__(self): 
        super(Explosion, self).__init__()
        self.image = pygame.image.load('Explosion.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()/10, self.image.get_height()/10))
        self.rect = self.image.get_rect()
        self.kill_timer = 30
        
    def update(self):
        if self.kill_timer == 0:
            self.kill()
        else:
            self.kill_timer -= 1