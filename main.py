import pygame
import random


class Pipe:
    def __init__(self):
        self.x = width
        self.opening_y = random.randint(0, height - 100)
        self.spawned_next_pipe = False
        self.rect_top = pygame.Rect(self.x, 0, 100, self.opening_y)
        self.rect_bottom = pygame.Rect(self.x, self.opening_y + 200, 100, height - (self.opening_y - 200))

    def draw(self, surface):
        self.x -= pipe_speed
        self.rect_top.x = self.x
        self.rect_bottom.x = self.x
        pygame.draw.rect(surface, GREEN, self.rect_top)
        pygame.draw.rect(surface, GREEN, self.rect_bottom)


class Bird:
    bird_size = 50
    gravity = 1

    def __init__(self):
        self.y = 100
        self.vel_y = 0
        self.rect = pygame.Rect(20, self.y, self.bird_size, self.bird_size)

    def draw(self, surface):
        if self.rect.y > height - self.bird_size:
            self.rect.y = height - self.bird_size
        if self.rect.y < height - self.bird_size:
            self.vel_y += self.gravity
        self.vel_y *= 0.9
        self.rect.y += self.vel_y
        pygame.draw.rect(surface, YELLOW, self.rect)


# Initialize game engine
pygame.init()

# Game colors
BLACK = 0, 0, 0
GREEN = 0, 200, 0
BLUE = 148, 189, 255
YELLOW = 255, 218, 148

# Window settings
size = width, height = 600, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappybird")

done = False
dead = False
clock = pygame.time.Clock()

# Bird
bird = Bird()

# Pipes
pipe_speed = 2
pipes = [Pipe()]

# Game loop
while not done:
    # 60 FPS
    clock.tick(60)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not dead:
                bird.vel_y -= 24

    # Rendering
    screen.fill(BLUE)
    bird.draw(screen)

    # Pipe spawning and destroying.
    if len(pipes) > 0:
        if pipes[0].x < width * 0.5 and pipes[0].spawned_next_pipe is False:
            pipes.append(Pipe())
            pipes[0].spawned_next_pipe = True
        if pipes[0].x < -100:
            pipes.pop(0)
    for i in range(len(pipes)):
        pipes[i].draw(screen)
        if bird.rect.colliderect(pipes[i].rect_top) or bird.rect.colliderect(pipes[i].rect_bottom):
            bird.vel_y = 0
            pipe_speed = 0
            dead = True

    pygame.display.flip()

pygame.quit()
