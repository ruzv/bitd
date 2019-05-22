import pygame
import game

pygame.init()
DISPLAY = pygame.display.set_mode([640, 840])
pygame.display.set_caption("bird")
CLOCK = pygame.time.Clock()

arena = game.Arena(DISPLAY, 20, 20)
bird = game.Bird(DISPLAY, arena)

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()
            if event.key == pygame.K_r:
                arena.update_left_spikes()
                arena.update_right_spikes()


def update():
    event_handler()
    bird.update()
    CLOCK.tick(10)

def draw():
    DISPLAY.fill([0, 0, 0])

    arena.draw()
    bird.draw()

    pygame.display.update()

while True:
    update()
    draw()