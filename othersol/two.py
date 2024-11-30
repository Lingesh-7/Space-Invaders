import pygame

import random



# Initialize the game

pygame.init()



# Screen dimensions

SCREEN_WIDTH = 800

SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



# Set title and icon

pygame.display.set_caption("Space Invaders")

icon = pygame.image.load('spaceship.png')  # Add an icon image in the same directory

pygame.display.set_icon(icon)



# Load player image

player_img = pygame.image.load('player.png')  # Add a player image in the same directory

player_x = 370

player_y = 480

player_x_change = 0



# Load alien image

alien_img = pygame.image.load('alien.png')  # Add an alien image in the same directory

alien_x = random.randint(0, SCREEN_WIDTH - 64)

alien_y = random.randint(50, 150)

alien_x_change = 4

alien_y_change = 40



# Bullet settings

bullet_img = pygame.image.load('bullet.png')  # Add a bullet image in the same directory

bullet_x = 0

bullet_y = 480

bullet_y_change = 10

bullet_state = "ready"  # "ready" means you can't see the bullet on the screen



# Score

score = 0

font = pygame.font.Font(None, 36)



# Function to show the score

def show_score(x, y):

    score_display = font.render("Score: " + str(score), True, (255, 255, 255))

    screen.blit(score_display, (x, y))



# Function to draw the player

def player(x, y):

    screen.blit(player_img, (x, y))



# Function to draw an alien

def alien(x, y):

    screen.blit(alien_img, (x, y))



# Function to fire a bullet

def fire_bullet(x, y):

    global bullet_state

    bullet_state = "fire"

    screen.blit(bullet_img, (x + 16, y + 10))



# Function to detect collision

def is_collision(alien_x, alien_y, bullet_x, bullet_y):

    distance = ((alien_x - bullet_x) ** 2 + (alien_y - bullet_y) ** 2) ** 0.5

    return distance < 27



# Game loop

running = True

while running:

    screen.fill((0, 0, 0))  # Fill the screen with black



    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False



        # Control player movement

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:

                player_x_change = -5

            if event.key == pygame.K_RIGHT:

                player_x_change = 5

            if event.key == pygame.K_SPACE:

                if bullet_state == "ready":

                    bullet_x = player_x

                    fire_bullet(bullet_x, bullet_y)



        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

                player_x_change = 0



    # Player movement

    player_x += player_x_change

    player_x = max(0, min(player_x, SCREEN_WIDTH - 64))  # Stay within screen bounds



    # Alien movement

    alien_x += alien_x_change

    if alien_x <= 0:

        alien_x_change = 4

        alien_y += alien_y_change

    elif alien_x >= SCREEN_WIDTH - 64:

        alien_x_change = -4

        alien_y += alien_y_change



    # Bullet movement

    if bullet_state == "fire":

        fire_bullet(bullet_x, bullet_y)

        bullet_y -= bullet_y_change



    # Check bullet collision with alien

    if bullet_y <= 0:

        bullet_y = 480

        bullet_state = "ready"



    if is_collision(alien_x, alien_y, bullet_x, bullet_y):

        bullet_y = 480

        bullet_state = "ready"

        score += 1

        alien_x = random.randint(0, SCREEN_WIDTH - 64)

        alien_y = random.randint(50, 150)



    # Draw everything

    player(player_x, player_y)

    alien(alien_x, alien_y)

    show_score(10, 10)



    pygame.display.update()  # Update the screen



pygame.quit()