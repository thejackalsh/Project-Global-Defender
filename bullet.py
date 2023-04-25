import pygame
from typing import Tuple
from pygame import mixer


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, y_offset: int, bullet_size: Tuple[int, int] = (15, 30)) -> None:
        super().__init__()
        self.image = pygame.image.load("bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, bullet_size)
        self.rect = self.image.get_rect()
        self.rect.centery = y + y_offset
        self.rect.centerx = x
        self.speed_y = -10
        self.bullet_sound = mixer.Sound("laser.mp3") # definisikan variabel bullet_sound di dalam kelas Bullet
        self.bullet_sound.stop()
        self.bullet_sound.play()  # play bullet sound when bullet is fired

    def update(self, *args: Tuple) -> None:
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()

