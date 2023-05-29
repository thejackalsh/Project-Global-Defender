import pygame
import constant as c
from hud import HUD

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Global Defender\Assets\Fighter.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()/7, self.image.get_height()/7))
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH - 339
        self.rect.y = c.DISPLAY_HEIGHT - 150
        self.max_hp = 3
        self.hp = self.max_hp
        self.hud = HUD(self.hp)
        self.hud_group = pygame.sprite.Group()
        self.hud_group.add(self.hud)
        self.lives = 3 
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        
    
    def update(self):
        self.hud_group.update()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
    def get_hit(self):
        self.hp -= 1
        self.hud.health_bar.decrease_hp_value()
        if self.hp <= 0: 
            self.hp = 0 
            self.death()
        print(self.hp)
        
    def death(self):
        self.lives -= 1 
        print(self.lives)
        if self.lives <= 0: 
            self.lives = 0 
        self.hp = self.max_hp
        self.hud.health_bar.reset_health_to_max()