import pygame
import random

def chance(c):
    if random.randint(0, 99) < c:
        return True
    else:
        return False

class Arena:


    def __init__(self, surface, x, y):
        self.surface = surface
        self.x = x
        self.y = y
        self.difficulty = 10

        self.update_left_spikes()
        self.update_right_spikes()

    def update_left_spikes(self):
        self.l_spikes = []
        for i in range(16):
            self.l_spikes.append(chance(self.difficulty))

    def update_right_spikes(self):
        self.r_spikes = []
        for i in range(16):
            self.r_spikes.append(chance(self.difficulty))

    def draw_left_spikes(self):
        for i in range(16):
            if self.l_spikes[i]:
                pygame.draw.rect(self.surface, (255, 255, 255), [self.x, self.y+(i*50)+2, 8, 46])

    def draw_right_spikes(self):
        for i in range(16):
            if self.r_spikes[i]:
                pygame.draw.rect(self.surface, (255, 255, 255), [self.x+592, self.y+(i*50)+2, 8, 46])

    def draw(self):
        #self.draw_left_spikes()
        #self.draw_right_spikes()
        pygame.draw.rect(self.surface, (255, 255, 255), [self.x, self.y, 600, 800], 1)


class Bird:

    def __init__(self, surface, arena):
        self.surface = surface
        self.arena = arena

        self.x = 0
        self.y = 0
        self.time = 0

        self.dx = 10
        self.dt = 0.1
        self.t = 0
        self.j = 20
        self.g = 12

        self.spawn()

    def spawn(self):
        #print(self.y)
        self.x = (600-50)/2
        self.y = (800-50)/2
        self.dx = abs(self.dx)
        self.t = 0

    def jump(self):
        self.t = 0

    def update(self):
        self.y -= (self.j-(self.g*self.t))
        self.x += self.dx
        self.t += self.dt

        if self.left_right_colision():

            self.dx = -self.dx
            self.arena.update_left_spikes()
            self.arena.update_right_spikes()


        if self.top_bottom_colision():
            self.spawn()

        if self.dx > 0:
            x = (self.x+25)/600
        else:
            x = (574-self.x)/600

        print(round((self.y+25)/800, 2), round((775-self.y)/800, 2), round(x, 2))

        return True

    def main(self):
        self.time = 0
        self.spawn()
        while update():
            self.time += 1

    def top_bottom_colision(self):
        if self.y < 0 or self.y > 800-50:
            return True

    def left_right_colision(self):
        if self.x <= 0 or self.x >= 600-50:
            return True

    def draw(self):
        pygame.draw.rect(self.surface, (255, 255, 255), [self.x+self.arena.x, self.y+self.arena.y, 50, 50])