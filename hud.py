import pygame
import constant as c
from health_bar import HealthBar  

class HUD(pygame.sprite.Sprite):
    def __init__(self, hp):
        super(HUD, self).__init__()
        self.image = pygame.image.load('hud.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH - 610
        self.rect.y = c.DISPLAY_HEIGHT - 40
        self.vel_x = 0
        self.vel_y = 0
        self.health_bar = HealthBar(hp)
        self.health_bar.rect.x = 22.5
        self.health_bar.rect.y = c.DISPLAY_HEIGHT - self.health_bar.rect.height - 17
        self.health_bar_group = pygame.sprite.Group()
        self.health_bar_group.add(self.health_bar)
    
    def update(self):
        self.health_bar_group.update()
        self.rect.x +=self.vel_x
        self.rect.y +=self.vel_y
        