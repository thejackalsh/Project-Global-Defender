import pygame
from explosion import Explosion


class ExplosionSpawner: 
    def __init__(self) -> None:
        self.explosion_group = pygame.sprite.Group()
        
    
    def  update(self):
        self.explosion_group.update()
    
    def spawn_explosion(self, pos):
        new_explosion = Explosion()
        new_explosion.rect.x = pos[0]
        new_explosion.rect.y = pos[1]
        self.explosion_group.add(new_explosion)