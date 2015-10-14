import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../illustration2vec")
import i2v

class Evaluator:

    def __init__(self, model, list):
        self.evaluator = i2v.make_i2v_with_chainer(model, list)

    def evaluate(self, gene, tags):
        result = self.evaluator.estimate_specific_tags([gene], tags)[0]
        return sum(result.values())

    def evaluate_all(self, genes, tags):
        results = self.evaluator.estimate_specific_tags(genes, tags)
        return [sum(r.values()) for r in results]
