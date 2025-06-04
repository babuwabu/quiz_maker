# Make it into a pygame
import pygame
import sys

# Initialize Pygame window and font
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lulu's Quiz Maker")

# Load pixel background and scale to screen
bg_image = pygame.image.load("pixel forest.jpg")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

# Load pixel font
font = pygame.font.Font("PressStart2P-Regular.ttf", 18)
large_font = pygame.font.Font("PressStart2P-Regular.ttf", 24)
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 150, 255)

# end