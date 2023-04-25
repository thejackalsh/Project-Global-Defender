import pygame
import constant as c

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Fighter.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width()/7, self.image.get_height()/7))
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH - 339
        self.rect.y = c.DISPLAY_HEIGHT - 150
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        
    
    def Sprite(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
