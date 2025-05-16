
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 480, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pacman = pygame.Rect(WIDTH//2, HEIGHT//2, 40, 40)
speed = 5
direction = pygame.Vector2(0, 0)

# On-screen controls (for mobile)
button_size = 60
buttons = {
    "left": pygame.Rect(40, HEIGHT - 100, button_size, button_size),
    "right": pygame.Rect(160, HEIGHT - 100, button_size, button_size),
    "up": pygame.Rect(100, HEIGHT - 160, button_size, button_size),
    "down": pygame.Rect(100, HEIGHT - 40, button_size, button_size),
}

def draw_controls():
    for key, rect in buttons.items():
        pygame.draw.rect(screen, (100, 100, 100), rect)
        pygame.draw.rect(screen, (200, 200, 200), rect, 3)

while True:
    screen.fill((0, 0, 0))
    draw_controls()
    pygame.draw.ellipse(screen, (255, 255, 0), pacman)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for key, rect in buttons.items():
                if rect.collidepoint(pos):
                    if key == "left": direction = (-1, 0)
                    elif key == "right": direction = (1, 0)
                    elif key == "up": direction = (0, -1)
                    elif key == "down": direction = (0, 1)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: direction = (-1, 0)
    if keys[pygame.K_RIGHT]: direction = (1, 0)
    if keys[pygame.K_UP]: direction = (0, -1)
    if keys[pygame.K_DOWN]: direction = (0, 1)

    pacman.x += direction.x * speed
    pacman.y += direction.y * speed

    pygame.display.flip()
    clock.tick(60)
