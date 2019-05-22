import environment
import net as n
import pygame

net = n.Net([1])

DISPLAY = pygame.display.set_mode([640, 840])
CLOCK = pygame.time.Clock()

env = environment.Environment(net, 1000, True, DISPLAY, CLOCK, 40, 20, 20, True)

env.main([0])