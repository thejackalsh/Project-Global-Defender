import pygame
import constant as c 
from background import BG
from ship import Ship
from bullet import Bullet
from enemy_spawner import EnemySpawner
from particle_spawner import ParticleSpawner 



# Game name
pygame.display.set_caption("Global Defender")

# Initialize pygame
pygame.init()
pygame.font.init()


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

# Particle Spawner 
particle_spawner= ParticleSpawner()



# Set the initial speed of the player's ship to 0
player_speed_x = 0
player_speed_y = 0

# Music setup
pygame.mixer.music.load('Global Defender\Assets\AC-DC Shoot to Thrill Instrumental.ogg')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(loops=-1)

# Load the custom font
font_path = r"Global Defender\Assets\AGRESSIVE.otf"
pause_font = pygame.font.Font(font_path, 20)

# Run the game loop
running = True
paused = False  # Initialize pause state
music_paused = False  # Initialize music pause state
music_pos = 0  # Variable to store the music position
while running:
    # Control the frame rate
    clock.tick(fps)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Handle key presses
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused  # Toggle pause state
                if paused:
                    pygame.mixer.music.pause()  # Pause the music
                else:
                    pygame.mixer.music.unpause()  # Resume the music
            elif event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx - 0.55, player.rect.top, y_offset= + 10)
                bullet_group.add(bullet)
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT or event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player_speed_x = 0
            elif event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player_speed_y = 0
    
    # If the game is paused, only update the display and continue to the next iteration
    if paused:
        display.fill(black)
        pause_text = pause_font.render("Game Paused", True, (255, 255, 255))
        display.blit(pause_text, (c.DISPLAY_SIZE[0] // 2 - pause_text.get_width() // 2, c.DISPLAY_SIZE[1] // 2 - pause_text.get_height() // 2))
        pygame.display.update()
        continue



    # Rest of the ship movement code
    player_speed_x = 0
    player_speed_y = 0

    # Update the player's ship position
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_speed_x = -5
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_speed_x = 5
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_speed_y = -5
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_speed_y = 5

    player.rect.x += player_speed_x
    player.rect.y += player_speed_y

    # Keep the player's ship within the screen boundaries
    if player.rect.left < 0:
        player.rect.left = 0
    elif player.rect.right > 600:
        player.rect.right = 600
    if player.rect.top < 0:
        player.rect.top = 0        
    elif player.rect.bottom > 760:
        player.rect.bottom = 760




    #Update the object 
    sprite_group.update()

    # Update the bullets
    bullet_group.update()

    # Update the background
    bg_group.update()

    # Update the enemy
    enemy_spawner.update()

    # Update the Particle
    particle_spawner.update()



    # Check collision
    collided = pygame.sprite.groupcollide(bullet_group, enemy_spawner.enemy_group, True, False)
    for bullet, enemy in collided.items():
        enemy[0].get_hit()
        player.hud.score.update_score(enemy[0].score_value)
        if not enemy[0].is_invincible:
            particle_spawner.spawn_particle((bullet.rect.x, bullet.rect.y))  
    collided = pygame.sprite.groupcollide(sprite_group, enemy_spawner.enemy_group, False, False)
    for player, enemy in collided.items():
        if not enemy[0].is_invincible:
            player.get_hit()
        enemy[0].hp = 0 
        enemy[0].get_hit()         



    #Render display
    # Update the game display
    display.fill(black)
    bg_group.draw(display)
    bullet_group.draw(display)
    sprite_group.draw(display)
    enemy_spawner.enemy_group.draw(display)
    particle_spawner.particle_group.draw(display)
    player.hud_group.draw(display)
    player.hud.health_bar_group.draw(display)
    player.hud.score_group.draw(display)
    pygame.display.update()



# Quit the game
pygame.quit()