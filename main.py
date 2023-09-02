# branch, this is branch creation 

class BinaryPerceptron(object):

    def __init__(self, examples, iterations):
        self.examples = examples
        self.iterations = iterations
        # See dimension (length of longest x_vector)
        d = 0
        for example in examples:
            x = example[0]
            if len(x) > d:
                d = len(example)
        # Build all zero initial omega
        self.omega = [0 for _ in range(d)]
        # self.omegas = dict()
        # self.omegas[True] = [0 for _ in range(d)]
        # self.omegas[False] = [0 for _ in range(d)]
        # Train the classifier for iterations times
        for _ in range(self.iterations):
            # print("Round ", _, " iteration")
            for example in self.examples:
                # print(example)
                x = example[0]
                y = example[1]
                y_hat = self.predict(x)
                if y_hat != y:
                    # print("y_hat: ", y_hat, " != ", "y: ", y)
                    self.omega_plus_x(example)
                    

    def predict(self, x):
        # score_true = 0
        # score_false = 0
        product = 0
        for key, value in x.items():
            d = int(key[1:])
            product = product + self.omega[d-1] * value
            # score_true = score_true + self.omegas[True][d-1] * value
            # score_false = score_false + self.omegas[False][d-1] * value
        if product > 0:
            return False
        else:
            return True


