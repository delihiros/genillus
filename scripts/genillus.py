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
        mating_pool = []
        s = 0.0
        best_score = 0
        best_image = 0
        for i in range(self.generation_set):
            print "evaluating ", i, "th image... ",
            self.generation[i].score = self.evaluator.evaluate(self.generation[i].as_image(), self.tags)
            print self.generation[i].score
            if best_score < self.generation[i].score:
                best_score = self.generation[i].score
                best_image = i
            s += self.generation[i].score

        print "saving best image"
        self.generation[best_image].as_image().save("generation_" + str(gen), ".png")

        print "making mating pool"
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
for i in range(10):
    print "step", i
    best_score = genillus.step(i)
    print "best score", best_score
    print "#############################"
