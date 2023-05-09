import pygame
from particle import Particle


class ParticleSpawner: 
    def __init__(self) -> None:
        self.particle_group = pygame.sprite.Group()
        
    
    def  update(self):
        self.particle_group.update()
    
    def spawn_particle(self, pos):
        new_particle = Particle()
        new_particle.rect.x = pos[0]
        new_particle.rect.y = pos[1]
        self.particle_group.add(new_particle)