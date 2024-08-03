import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake parameters
snake_size = 20
snake_speed = 15

# Set up the clock
clock = pygame.time.Clock()

# Define font
font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont(None, 35)

# Define snake function
def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(window, green, [pixel[0], pixel[1], snake_size, snake_size])

# Define food function
def draw_food(food_x, food_y, snake_size):
    pygame.draw.rect(window, red, [food_x, food_y, snake_size, snake_size])

# Define score function
def draw_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    window.blit(value, [0, 0])

# Game loop
def game_loop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_pixels = []
    snake_length = 1

    food_x = round(random.randrange(0, width - snake_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - snake_size) / 20.0) * 20.0

    score = 0

    while not game_over:

        while game_close == True:
            window.fill(black)
            message = font_style.render("You lost! Press Q-Quit or C-Play Again", True, red)
            window.blit(message, [width / 6, height / 3])
            draw_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(black)

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_pixels.append(snake_head)
        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == snake_head:
                game_close = True

        draw_snake(snake_size, snake_pixels)
        draw_food(food_x, food_y, snake_size)

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - snake_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - snake_size) / 20.0) * 20.0
            snake_length += 1
            score += 1

        draw_score(score)
        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
