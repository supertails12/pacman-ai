import pygame
import random
import sys

pygame.init()

# Constants
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
WIDTH = CELL_SIZE * GRID_WIDTH
HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS = 10

# Colors
GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)
RED = (255, 0, 0)
GOLD = (255, 215, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ultimate Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 24)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(5, 5)]
        self.direction = (1, 0)
        self.grow = False

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        if new_head in self.body or not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT):
            return False
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        return True

    def change_direction(self, new_dir):
        if (new_dir[0] * -1, new_dir[1] * -1) != self.direction:
            self.direction = new_dir

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Apple class
class Apple:
    def __init__(self):
        self.respawn()

    def respawn(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        self.is_golden = random.random() < 0.1
        self.timer = FPS * 5 if self.is_golden else 0

    def draw(self):
        color = GOLD if self.is_golden else RED
        pygame.draw.rect(screen, color, (self.position[0]*CELL_SIZE, self.position[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Draw text
def draw_text(text, x, y, color=WHITE):
    render = font.render(text, True, color)
    screen.blit(render, (x, y))

# Main game
def main():
    snake = Snake()
    apple = Apple()
    score = 0
    speed = FPS
    running = True

    while running:
        clock.tick(speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))

        if not snake.move():
            break  # Game Over

        if snake.body[0] == apple.position:
            snake.grow = True
            score += 50 if apple.is_golden else 10
            speed = min(speed + 0.2, 30)
            apple.respawn()

        if apple.is_golden:
            apple.timer -= 1
            if apple.timer <= 0:
                apple.respawn()

        screen.fill(BLACK)
        snake.draw()
        apple.draw()
        draw_text(f"Score: {score}", 10, 10)
        pygame.display.flip()

    # Game over screen
    screen.fill(BLACK)
    draw_text("Game Over!", WIDTH // 2 - 100, HEIGHT // 2 - 30)
    draw_text(f"Final Score: {score}", WIDTH // 2 - 100, HEIGHT // 2)
    pygame.display.flip()
    pygame.time.wait(2000)

# Run game
if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
