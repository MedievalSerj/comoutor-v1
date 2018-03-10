from math import sqrt


class Solver:

    D_MESSAGE_POSITIVE = ('Discriminant is strictly positive,'
                          ' the two solutions are:')
    D_MESSAGE_ZERO = 'Discriminant is zero, the solution is:'
    D_MESSAGE_NEGATIVE = ('Discriminant is negative,'
                          ' the complex solutions are:')

    def __init__(self, equation):
        self.equation = equation
        self.a = equation[2][0]
        self.b = equation[1][0]
        self.c = equation[0][0]
        self.D = self._get_discriminant()

    def get_discriminant_msg(self):
        if self.D > 0:
            return Solver.D_MESSAGE_POSITIVE
        elif self.D == 0:
            return Solver.D_MESSAGE_ZERO
        else:
            return Solver.D_MESSAGE_NEGATIVE

    @property
    def solution(self):
        if self.D > 0:
            solution = self._solve_positive()
            return f'{solution[0]}\n{solution[1]}'
        elif self.D == 0:
            solution = self._solve_zero()
            return f'{solution}'
        else:
            solution = self._solve_im()
            return f'{solution[0]} + j{solution[1]}\n' \
                   f'{solution[0]} - j{solution[1]}'

    def _get_discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def _solve_positive(self):
        return ((-self.b + sqrt(self.D)) / (2 * self.a),
                (-self.b - sqrt(self.D)) / (2 * self.a))

    def _solve_zero(self):
        return (-self.b) / (2 * self.a)

    def _solve_im(self):
        re = (-self.b) / (2 * self.a)
        im = sqrt(abs(self.D)) / (2 * self.a)
        return (re, im)
