import pygame
import constant as c
import pygame.font



class Score(pygame.sprite.Sprite):
    def __init__(self):
        super(Score, self).__init__()
        self.value = 0 
        self.font_size = 18 
        self.color = (0, 0, 0)
        font_path = r"AGRESSIVE.otf"
        self.font = pygame.font.Font(font_path, self.font_size)
        
        self.x_pad = 60 
        self.y_pad = 8
        
        self.image = self.font.render(str(f'Score: {self.value}'), False, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH - self.rect.width  - self.x_pad
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height  - self.y_pad
        
    def update(self):
        pass
    
    def update_score(self, value):
        self.value += value
        self.image = self.font.render(str(f'Score: {self.value}'),False, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH - self.rect.width - self.x_pad
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height - self.y_pad