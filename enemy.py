import pygame 
import constant as c 
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.img_explosion_1 = pygame.image.load('Explosion1.png').convert_alpha()
        self.img_explosion_1 = pygame.transform.scale(self.img_explosion_1, (self.img_explosion_1.get_width()/4, self.img_explosion_1.get_height()/4))
        self.img_explosion_2 = pygame.image.load('Explosion2.png').convert_alpha()
        self.img_explosion_2 = pygame.transform.scale(self.img_explosion_2, (self.img_explosion_2.get_width()/4, self.img_explosion_2.get_height()/4))
        self.img_explosion_3 = pygame.image.load('Explosion3.png').convert_alpha()
        self.img_explosion_3 = pygame.transform.scale(self.img_explosion_3, (self.img_explosion_3.get_width()/4, self.img_explosion_3.get_height()/4))
        
        self.anim_explosion = [self.img_explosion_1,
                                self.img_explosion_2,
                                self.img_explosion_3,]

        self.anim_index = 0 
        self.frame_lenght = 6
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
        if self.is_destroyed: 
            max_index = len(self.anim_explosion) - 1
            if self.anim_index > max_index: 
                self.kill()
            else: 
                if self.frame_lenght == 0: 
                    self.image = self.anim_explosion[self.anim_index]
                    self.anim_index += 1
                    self.frame_lenght = 6
                else: 
                    self.frame_lenght -=1     


    def get_hit(self): 
        if not self.is_invincible:
            self.hit_sound.play()
            self.hp -=1
            if self.hp <= 0:
                self.is_invincible = True
                self.is_destroyed = True 
                self.rect.x = self.rect.x - 18
                self.rect.y = self.rect.y - 20
                self.image = self.anim_explosion[self.anim_index]
                
