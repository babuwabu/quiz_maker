# Make it into a pygame
import pygame
import sys

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("02. Title Theme.mp3") 
pygame.mixer.music.set_volume(0.3)      
pygame.mixer.music.play(-1) 

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

# Ask user for the file name using text input
labels = ["Question", "a)", "b)", "c)", "d)", "Correct Answer (a/b/c/d)"] # Labels
inputs = [""] * len(labels)
current_input = 0
name = ""

# App states
file_named = False
adding_question = True
show_saved_message = False

def draw_text(text, x, y, font, color=BLACK):
    text_surf = font.render(text, True, color)
    screen.blit(text_surf, (x, y))

def save_question_to_file(name, data):
    with open(name, "a") as file:
      
        file.write("::QUESTION::\n")
        file.write(data[0] + "\n")
        file.write("a) " + data[1] + "\n")
        file.write("b) " + data[2] + "\n")
        file.write("c) " + data[3] + "\n")
        file.write("d) " + data[4] + "\n")
        file.write("ANSWER: " + data[5].lower() + "\n")
        file.write("::END::\n\n")

# While the user wants to add questions:
running = True
while running:
    screen.blit(bg_image, (0, 0)) 

# end
pygame.quit()
sys.exit()