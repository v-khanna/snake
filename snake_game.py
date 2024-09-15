import pygame
import sys
import random
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
GREEN = (35, 45, 40)
RED = (213, 50, 80)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock
clock = pygame.time.Clock()

# Font
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# High Score File
HIGH_SCORE_FILE = "high_score.txt"


def read_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as file:
            try:
                return int(file.read())
            except:
                return 0
    else:
        return 0


def write_high_score(score):
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(score))


def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, WHITE)
    screen.blit(value, [0, 0])


def display_high_score(high_score):
    value = score_font.render("High Score: " + str(high_score), True, WHITE)
    screen.blit(value, [0, 40])


def game_over_message():
    msg = font_style.render("Game Over! Press C-Play Again or Q-Quit", True, RED)
    screen.blit(msg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])


def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], snake_block, snake_block])


def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [x, y])


def gameLoop():
    high_score = read_high_score()

    game_over = False
    game_close = False

    snake_block = 10
    snake_speed = 15

    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            screen.fill(GREEN)
            game_over_message()
            display_score(Length_of_snake - 1)
            display_high_score(high_score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change

        # Screen wrapping logic
        if x1 >= SCREEN_WIDTH:
            x1 = 0
        elif x1 < 0:
            x1 = SCREEN_WIDTH - snake_block
        if y1 >= SCREEN_HEIGHT:
            y1 = 0
        elif y1 < 0:
            y1 = SCREEN_HEIGHT - snake_block

        screen.fill(GREEN)
        pygame.draw.rect(screen, RED, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake(snake_block, snake_List)
        display_score(Length_of_snake - 1)
        display_high_score(high_score)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
            foody = (
                round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 10.0) * 10.0
            )
            Length_of_snake += 1
            if Length_of_snake - 1 > high_score:
                high_score = Length_of_snake - 1
                write_high_score(high_score)

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()


def main_menu():
    while True:
        screen.fill(GREEN)
        message("Welcome to Snake Game", BLACK, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3)
        message(
            "Press S to Start Game", BLACK, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3 + 30
        )
        message(
            "Press H to View High Score",
            BLACK,
            SCREEN_WIDTH / 3,
            SCREEN_HEIGHT / 3 + 60,
        )
        message("Press Q to Quit", BLACK, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3 + 90)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    gameLoop()
                elif event.key == pygame.K_h:
                    show_high_score()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


def show_high_score():
    high_score = read_high_score()
    viewing = True
    while viewing:
        screen.fill(GREEN)
        display_high_score(high_score)
        message("Press B to go back", BLACK, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                viewing = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    viewing = False


if __name__ == "__main__":
    main_menu()
