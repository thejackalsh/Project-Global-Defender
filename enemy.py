import pygame 
import constant as c 
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('Alien.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()/7, self.image.get_height()/7))
        self.is_destroyed = False
        self.is_invincible = False
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.hit_sound = pygame.mixer.Sound('Metal Bat Hits Baseball.mp3')
        self.hp = 3
        self.vel_x = 0
        self.vel_y = random.randrange(3,4)
        
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


    def get_hit(self): 
        if not self.is_invincible:
            self.hit_sound.play()
            self.hp -=1
            if self.hp <= 0:
                self.is_invincible = True
                self.is_destroyed = True 
                self.destroy()


    def destroy(self):
        self.kill()