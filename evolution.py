import random
from copy import copy


class Population:


    def __init__(self, size, dna_lenght, fitness_fuction, selection, kill_rate):
        self.size = size
        self.dna_lenght = dna_lenght
        self.fitness_fuction = fitness_fuction
        self.selection = selection
        self.kill_rate = kill_rate

        self.generate_population()

    def evaluation(self, dna):
        score = 0
        for i in range(20):
            score += self.fitness_fuction(dna)
        return round(score/20, 0)


    def generate_population(self):
        self.population = []

        for i in range(self.size):
            dna = [random.random() for k in range(self.dna_lenght)]
            f = self.evaluation(dna)
            self.population.append([f, dna])

        return self.population

    def pick_entity(self):
        return int(random.random()*random.random()*(self.size-1))

    def breed(self):
        p1 = self.population[self.pick_entity()][1]
        p2 = self.population[self.pick_entity()][1]
        cuts = [random.randint(0, self.dna_lenght-1), random.randint(0, self.dna_lenght-1)]
        cuts.sort()
        p = p1[0:cuts[0]]+p2[cuts[0]:cuts[1]]+p1[cuts[1]:]
        return p

    def mutate(self, dna, d, m):
        multiplyers = [-1, 1]
        for i in range(m):
            dna[random.randint(0, self.dna_lenght-1)] += multiplyers[random.randint(0, 1)]*d
        return dna

    def visual(self):
        print(self.population[0][0], len(self.population))


    def evolve(self, v=False):


        self.population.sort()
        self.population.reverse() #larges to smalest

        if v:
            self.visual()

        new_entity_count = int((self.size)/self.kill_rate)

        new_population = []
        for i in range(self.size-new_entity_count):
            f = self.evaluation(self.population[i][1])
            new_population.append([f, self.population[i][1]])


        for i in range(new_entity_count):
            dna = self.breed()
            dna = self.mutate(dna, random.random(), 100)
            f = self.evaluation(dna)
            new_population.append([f, dna])

        self.population = copy(new_population)


