

class Solver:

    def __init__(self, equation):
        self.equation = equation

    def _filter_powers(self, power):
        filter(lambda x: x[1] == 0, self.equation)

    def reduce(self):
        zero_povers = filter(lambda x: x[1] == 0, self.equation)

