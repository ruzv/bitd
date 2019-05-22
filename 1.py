import net as n
import evolution
import environment
import pygame



#pygame.init()
#DISPLAY = pygame.display.set_mode([640, 840])
#CLOCK = pygame.time.Clock()


net = n.Net([8, 15, 1])
env = environment.Environment(net, 10000)
#visual_env = environment.Environment(net, 10000, True, DISPLAY, CLOCK, 100, 20, 20)
evo = evolution.Population(100, net.get_pram_len(), env.main, 1, 8)

for i in range(100):
    evo.evolve(True)
    #visual_env.main(evo.population[0][1])


evo.population.sort()
evo.population.reverse()
print(evo.population[0])