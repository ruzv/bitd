import linear_alg as lin
import math


class Net:

    def __init__(self, layers):
        self.layers = layers

        self.generate_biases()
        self.generate_weights()


    def generate_biases(self):
        self.biases = []
        for i in self.layers[1:]:
            self.biases.append([0 for x in range(i)])

    def generate_weights(self):
        self.weights = []
        for x, y in zip(self.layers[0:-1], self.layers[1:]):
            self.weights.append(lin.generate_matrix(x, y, 0))

    def feedforward(self, a):
        for w, b in zip(self.weights, self.biases):
            a = lin.el_func(lin.add(lin.m_v_mult(w, a), b), self.sigmoid)
        return a

    def forward_propogate(self, a):
        activations = [a]
        for w, b in zip(self.weights, self.biases):
            a = lin.el_func(lin.add(lin.m_v_mult(w, a), b), self.sigmoid)
            activations.append(a)
        return activations

    def binary_feedforward(self, a, threshold):
        for w, b in zip(self.weights, self.biases):
            a = lin.el_func(lin.add(lin.m_v_mult(w, a), b), self.sigmoid)
        na = []
        for i in a:
            if i >= threshold:
                na.append(True)
            else:
                na.append(False)
        return na

    def sigmoid(self, z):
        return 1/(1+math.exp(-z))

    def get_pram_len(self):
        l = 0
        for x, y in zip(self.layers[0:-1], self.layers[1:]):
            l += x*y
            l += y
        return l

    def set_prams(self, dna):
        i = 0
        self.weights = []
        for x, y in zip(self.layers[0:-1], self.layers[1:]):
            w = []
            for yi in range(y):
                l = []
                for xi in range(x):
                    l.append(dna[i])
                    i += 1
                w.append(l)
            self.weights.append(w)

        self.biases = []
        for x in self.layers[1:]:
            b = []
            for xi in range(x):
                b.append(dna[i])
                i += 1
            self.biases.append(b)

