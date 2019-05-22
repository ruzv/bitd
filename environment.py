import pygame
import random
import net as n

def ground(b, t, v):
    if v < b:
        return b
    elif v > t:
        return t
    else:
        return v


class Environment:

    def __init__(self, net, threshold, is_draw=False, surface=None, clock=None, tick=0, screen_x=0, screen_y=0, is_user=False):
        self.net = net
        self.threshold = threshold

        self.x = 0
        self.y = 0
        self.time = 0
        self.difficulty = 20
        self.beams_points = [-80, -40, 0, 40, 80]
        self.left_spikes = self.gen_spikes()
        self.right_spikes = self.gen_spikes()

        self.dx = 10
        self.dt = 0.1
        self.t = 0

        self.is_draw = is_draw
        self.surface = surface
        self.clock = clock
        self.tick = tick
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.is_user = is_user

    def gen_spikes(self):
        spikes = []
        for i in range(10):
            if random.randint(0, 100) <= self.difficulty:
                spikes.append(True)
            else:
                spikes.append(False)
        return spikes

    def spawn(self):
        self.x = (600-50)/2
        self.y = (800-50)/2
        self.dx = abs(self.dx)
        self.t = 0
        self.time = 0
        self.left_spikes = self.gen_spikes()
        self.right_spikes = self.gen_spikes()

    def jump(self):
        self.t = 0

    def update(self):
        self.y -= (20-(12*self.t))
        self.x += self.dx
        self.t += self.dt

        if self.left_right_colision():
            if self.spike_colision():
                return False

            self.dx = -self.dx
            self.left_spikes = self.gen_spikes()
            self.right_spikes = self.gen_spikes()

        if self.top_bottom_colision():
            return False

        beams = []
        for b in self.beams_points:
            if self.dx > 0:
                if self.right_spikes[ground(0, 9, int((self.y+b)/80))]:
                    beams.append(1)
                else:
                    beams.append(0)
            else:
                if self.left_spikes[ground(0, 9, int((self.y+b)/80))]:
                    beams.append(1)
                else:
                    beams.append(0)

        if self.dx > 0:
            x = (self.x+25)/600
        else:
            x = (575-self.x)/600
        self.a = [round((self.y+25)/800, 2), round((775-self.y)/800, 2), round(x, 2)] # net input
        self.a += beams

        return True

    def spike_colision(self):
        points = [0, 24, 49]

        for p in points:
            for i in range(10):
                if self.dx > 0:
                    if self.right_spikes[i]:
                        if self.y+p>=(i*80)+20 and self.y+p<=(i*80)+60:
                            return True
                else:
                    if self.left_spikes[i]:
                        if self.y+p>=(i*80)+20 and self.y+p<=(i*80)+60:
                            return True

        return False

    def top_bottom_colision(self):
        if self.y < 0 or self.y > 800-50:
            return True

    def left_right_colision(self):
        if self.x <= 0 or self.x >= 600-50:
            return True

    def main(self, dna):
        self.net.set_prams(dna)
        self.spawn()

        while self.update():
            self.time += 1
            o = self.net.binary_feedforward(self.a, 0.5)

            if self.is_user:
                self.user_controle()
            elif o[0]:
                self.jump()

            if self.is_draw:
                self.draw()
                self.clock.tick(self.tick)

            if self.time > self.threshold:
                break

        return self.time

    def user_controle(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.jump()

    def draw(self):
        self.surface.fill([0, 0, 0])
        pygame.draw.rect(self.surface, (255, 255, 255), [self.screen_x, self.screen_y, 600, 800], 1)
        for i in range(len(self.beams_points)):
            if self.dx > 0:
                pygame.draw.line(self.surface, (255, 0, 0), [self.x+self.screen_x+25, self.y+self.screen_y+25+self.beams_points[i]], [600+self.screen_x, self.y+self.screen_y+25+self.beams_points[i]])
            else:
                pygame.draw.line(self.surface, (255, 0, 0), [self.x+self.screen_x+25, self.y+self.screen_y+25+self.beams_points[i]], [self.screen_x, self.y+self.screen_y+25+self.beams_points[i]])

        pygame.draw.rect(self.surface, (255, 255, 255), [self.x+self.screen_x, self.y+self.screen_y, 50, 50])
        for i in range(10):
            if self.left_spikes[i]:
                pygame.draw.rect(self.surface, (255, 255, 255), [self.screen_x, self.screen_y+(80*i)+20, 8, 40])
            if self.right_spikes[i]:
                pygame.draw.rect(self.surface, (255, 255, 255), [self.screen_x+600-8, self.screen_y+(80*i)+20, 8, 40])
        pygame.display.update()

