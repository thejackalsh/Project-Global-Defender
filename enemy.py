import pygame 
import constant as c 
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('Alien.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()/7, self.image.get_height()/7))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.vel_x = 0
        self.vel_y = random.randrange(4,8)
        
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        