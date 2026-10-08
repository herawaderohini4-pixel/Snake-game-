import pygame
import random
import sys

pygame.init()

WIDTH = 600
HEIGHT = 500
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

BLACK = (20, 20, 20)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 120, 0)
RED = (255, 60, 60)
WHITE = (255, 255, 255)

font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 60)
clock = pygame.time.Clock()
FPS = 10

def create_food(snake):
    while True:
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)
        if (x, y) not in snake:
            return (x, y)

def draw_snake(snake):
    for i, part in enumerate(snake):
        color = DARK_GREEN if i == 0 else GREEN
        pygame.draw.rect(screen, color, (part[0], part[1], CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def game_over_screen(score):
    screen.fill(BLACK)
    items = [
        (big_font.render("GAME OVER!", True, RED), 150),
        (font.render(f"Final Score: {score}", True, WHITE), 220),
        (font.render("Press R to Replay", True, WHITE), 280),
        (font.render("Press Q to Quit", True, WHITE), 320),
    ]
    for text, y in items:
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, y))
    pygame.display.update()

def play_game():
    snake = [(300, 240), (280, 240), (260, 240)]
    direction = "RIGHT"
    food = create_food(snake)
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        head_x, head_y = snake[0]
        if direction == "UP":
            head_y -= CELL_SIZE
        elif direction == "DOWN":
            head_y += CELL_SIZE
        elif direction == "LEFT":
            head_x -= CELL_SIZE
        elif direction == "RIGHT":
            head_x += CELL_SIZE

        new_head = (head_x, head_y)

        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            return score

        if new_head in snake:
            return score

        snake.insert(0, new_head)

        if new_head == food:
            score += 10
            food = create_food(snake)
        else:
            snake.pop()

        screen.fill(BLACK)
        draw_food(food)
        draw_snake(snake)
        show_score(score)
        pygame.display.update()
        clock.tick(FPS)

while True:
    final_score = play_game()
    game_over_screen(final_score)

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
