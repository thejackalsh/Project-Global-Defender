import pygame
import constant as c 
from background import BG
from ship import Ship
from bullet import Bullet
from enemy_spawner import EnemySpawner
from explosion_spawner import ExplosionSpawner 


# Game name
pygame.display.set_caption("Global Defender")

# Initialize pygame
pygame.init()



# Set the dimensions of the display
display = pygame.display.set_mode((c.DISPLAY_SIZE))

# Create a clock object to help control the frame rate
clock = pygame.time.Clock()

#Color
black = (0, 0, 0)

# Set the frames per second
fps = 60



#Background 
bg = BG()
bg_group = pygame.sprite.Group()

# Add the Background instance to the sprite group
bg_group.add(bg)


# PLAYER PLAYER PLAYER PLAYER 
# Create the player's ship
player = Ship()
player_group = pygame.sprite.Group()

# Add the Ship instance to the sprite group
player_group.add(player)

# Create a sprite group for the bullets
bullet_group = pygame.sprite.Group()

# Sprite group
sprite_group = pygame.sprite.Group()
sprite_group.add(player)

# Enemy Spawner
enemy_spawner = EnemySpawner()

# Explosion Spawner 
explosion_spawner= ExplosionSpawner()




# Set the initial speed of the player's ship to 0
player_speed_x = 0
player_speed_y = 0

# Music setup
pygame.mixer.music.load('Metallica-Better-Than-You-instrumental.ogg')
pygame.mixer.music.set_volume(.2)
pygame.mixer.music.play(loops=True)


# Run the game loop
running = True
while running:
    # Control the frame rate
    clock.tick(fps)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Ship Movement
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player_speed_x = -5
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player_speed_x = 5
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player_speed_y = -5
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player_speed_y = 5
            elif event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx - 0.55, player.rect.top, y_offset= + 10)
                bullet_group.add(bullet)
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT or event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player_speed_x = 0
            elif event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player_speed_y = 0


    # Update the player's ship position
    player.rect.x += player_speed_x
    player.rect.y += player_speed_y


    # Keep the player's ship within the screen boundaries
    if player.rect.left < 0:
        player.rect.left = 0
    elif player.rect.right > 600:
        player.rect.right = 600
    if player.rect.top < 0:
        player.rect.top = 0        
    elif player.rect.bottom > 770:
        player.rect.bottom = 770

    

    #Update the object 
    sprite_group.update()

    # Update the bullets
    bullet_group.update()

    # Update the background
    bg_group.update()

    # Update the enemy
    enemy_spawner.update()

    # Update the explosion 
    explosion_spawner.update()


    # Check collision
    collided = pygame.sprite.groupcollide(bullet_group, enemy_spawner.enemy_group, True, False)
    for bullet, enemy in collided.items():
        enemy[0].get_hit()
        explosion_spawner.spawn_explosion((bullet.rect.x, bullet.rect.y))  
    collided = pygame.sprite.groupcollide(sprite_group, enemy_spawner.enemy_group, False, False)
    for player, enemy in collided.items():
        if not enemy[0].is_invincible:
            player.get_hit()
        enemy[0].hp = 0 
        enemy[0].get_hit()
        


    #Render display
    display.fill(black)
    bg_group.draw(display)
    bullet_group.draw(display)
    sprite_group.draw(display)
    enemy_spawner.enemy_group.draw(display)
    explosion_spawner.explosion_group.draw(display)
    player.hud_group.draw(display)
    player.hud.health_bar_group.draw(display)
    pygame.display.update()



# Quit the game
pygame.quit()