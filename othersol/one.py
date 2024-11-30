import pygame

import random



# Initialize Pygame

pygame.init()



# Constants

WIDTH, HEIGHT = 800, 600

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

FPS = 60

PLAYER_SPEED = 5

BULLET_SPEED = 7

ENEMY_SPEED = 1



# Set up the display

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Space Invaders")



# Load images

player_image = pygame.Surface((50, 50))  # Placeholder for the player ship

player_image.fill(WHITE)

enemy_image = pygame.Surface((50, 50))  # Placeholder for enemy ship

enemy_image.fill((255, 0, 0))



# Classes

class Player:

    def __init__(self):

        self.image = player_image

        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))

   

    def move(self, dx):

        if 0 < self.rect.x + dx < WIDTH - self.rect.width:

            self.rect.x += dx

   

    def draw(self):

        screen.blit(self.image, self.rect)



class Bullet:

    def __init__(self, x, y):

        self.rect = pygame.Rect(x, y, 5, 10)

   

    def move(self):

        self.rect.y -= BULLET_SPEED

   

    def draw(self):

        pygame.draw.rect(screen, WHITE, self.rect)



class Enemy:

    def __init__(self, x, y):

        self.image = enemy_image

        self.rect = self.image.get_rect(topleft=(x, y))

   

    def move(self):

        self.rect.y += ENEMY_SPEED

   

    def draw(self):

        screen.blit(self.image, self.rect)

