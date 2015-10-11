import sys
import numpy as np
from PIL import Image

class DNA:

    def __init__(self):
        pass

    def from_image(self, image):
        self.gene = np.asarray(image, dtype=np.float32)
        if self.gene.ndim == 2:
            self.gene = np.empty((self.gene.shape[0], self.gene.shape[1], 3), dtype=np.float32)
            self.gene[:] = self.gene.reshape(self.gene.shape[0], self.gene.shape[1], 1)
        elif self.gene.ndim == 3:
            self.gene = self.gene[:,:,:3]
        else:
            raise TypeError("unsupported image!")

    def as_image(self):
        return Image.fromarray(self.gene)

    def wellness(self, evaluator):
        return evaluator.evaluate(self.gene)

    def crossover(self, dna):
        child = DNA()
        return child

    def mutate(self, mutation_rate):
        pass


delihiros = Image.open("./resources/delihiros.png")
dna = DNA()
dna.from_image(delihiros)
print dna.gene
