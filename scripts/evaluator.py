import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../illustration2vec")
print os.path.dirname(os.path.abspath(__file__)) + "/illustration2vec"
import i2v

class Evaluator:

    def __init__(self, model, list):
        self.evaluator = i2v.make_i2v_with_chainer(model, list)

    def evaluate(self, image, tags):
        result = self.evaluator.estimate_specific_tags([img], tags)[0]
        return sum(result.values)
