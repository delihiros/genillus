import sys, random
import numpy as np
from PIL import Image

class DNA:

    def __init__(self, size=(320,320,4)):
        self.size = size
        self.gene = np.random.randint(0, high=255, size=size)
        self.gene[:,:,3] = 255

    def as_image(self):
        return Image.fromarray(self.gene, 'RGBA')

    def crossover(self, partner):
        child = DNA(size=self.size)
        for i in range(len(self.gene)):
            midpoint = np.random.randint(0, high=len(self.gene[i]))
            for j in range(len(self.gene[i])):
                if j > midpoint: child.gene[i,j] = self.gene[i,j]
                else: child.gene[i,j] = partner.gene[i,j]
        return child

    def mutate(self, mutation_rate):
        for i in range(len(self.gene)):
            for j in range(len(self.gene[i])):
                if (random.random() < mutation_rate):
                    self.gene[i,j] = np.random.randint(0, high=255, size=4)
                    self.gene[i,j,3] = 255
