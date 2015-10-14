import sys, os, random
import dna
import evaluator

class Genillus:

    def __init__(self, evaluator, tags, size=(320,320,3), generation_set=200, mutation_rate=0.01):
        self.evaluator = evaluator
        self.tags = tags
        self.generation_set = generation_set
        self.generation = []
        for i in range(generation_set):
            self.generation.append(dna.DNA(size=size))
    
    def step(self, gen):
        s = 0.0
        best_score = 0
        best_image = None

        scores = self.evaluator.evaluate_all([c.as_image() for c in self.generation], self.tags)
        for i, (c, score) in enumerate(zip(self.generation, scores)):
            print i, c, score
            c.score = score
            s += score
            if best_score < score:
                best_score = score
                best_image = c

        print "saving best image"
        best_image.as_image().save("generation_" + str(gen) + ".png")

        print "making mating pool"
        mating_pool = []
        for i in range(self.generation_set):
            n = int(self.generation[i].score / s)
            for j in range(n):
                mating_pool.append(self.generation[i])
        
        print "crossovering"
        for i in range(self.generation_set):
            a = random.choice(mating_pool)
            b = random.choice(mating_pool)
            child = a.crossover(b)
            child.mutate(self.mutation_rate)
            self.generation[i] = child

        return best_score


print "making evaluator"
ev = evaluator.Evaluator(
        os.path.dirname(os.path.abspath(__file__)) + "/../illustration2vec/illust2vec_tag_ver200.caffemodel",
        os.path.dirname(os.path.abspath(__file__)) + "/../illustration2vec/tag_list.json"
        )
print "done making evaluator"

print "making genillus"
genillus = Genillus(ev, ["hatsune miku"], size=(100, 100, 3))
print "done making genillus"
for i in range(100):
    print "step", i
    best_score = genillus.step(i)
    print "best score", best_score
    print "#############################"
