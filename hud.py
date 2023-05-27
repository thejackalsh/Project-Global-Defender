import pygame
import constant as c
from health_bar import HealthBar  
from score import Score

class HUD(pygame.sprite.Sprite):
    def __init__(self, hp):
        super(HUD, self).__init__()
        self.image = pygame.image.load('hud.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*2.4   , self.image.get_height()*1.7))
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH - 659
        self.rect.y = c.DISPLAY_HEIGHT - 43.5
        self.vel_x = 0
        self.vel_y = 0
        self.health_bar = HealthBar(hp)
        self.health_bar.rect.x = 15
        self.health_bar.rect.y = c.DISPLAY_HEIGHT - self.health_bar.rect.height - 10
        self.health_bar_group = pygame.sprite.Group()
        self.health_bar_group.add(self.health_bar)
        self.score = Score()
        self.score_group = pygame.sprite.Group()
        self.score_group.add(self.score)
        
    
    def update(self):
        self.health_bar_group.update()
        self.score_group.update()
        self.rect.x +=self.vel_x
        self.rect.y +=self.vel_y
        