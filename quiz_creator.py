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

# end