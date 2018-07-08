from math import sqrt


class Solver:

    D_MESSAGE_POSITIVE = ('Discriminant is strictly positive,'
                          ' the two solutions are:')
    D_MESSAGE_ZERO = 'Discriminant is zero, the solution is:'
    D_MESSAGE_NEGATIVE = ('Discriminant is negative,'
                          ' the complex solutions are:')

    def __init__(self, equation):
        self.equation = equation.equation
        self.degree = equation.degree
        self.a = self.equation[2][0]
        self.b = self.equation[1][0]
        self.c = self.equation[0][0]
        self.D = self._get_discriminant()

    def print_discriminant_msg(self):
        if self.degree < 2:
            return
        if self.D > 0:
            msg = Solver.D_MESSAGE_POSITIVE
        elif self.D == 0:
            msg = Solver.D_MESSAGE_ZERO
        else:
            msg = Solver.D_MESSAGE_NEGATIVE
        print(msg)

    @property
    def solution(self):
        if (self.degree == 0 and self.equation[0][0] == 0
                and self.equation[1][0] == 0
                and self.equation[2][0] == 0):
            return 'All real numbers are solutions'
        elif self.degree == 0:
            return 'This is not even an equation'
        elif self.degree == 1:
            return self._solve_linear()
        elif self.D > 0:
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

    def _solve_linear(self):
        return -self.c / self.b

    def _solve_positive(self):
        return ((-self.b + sqrt(self.D)) / (2 * self.a),
                (-self.b - sqrt(self.D)) / (2 * self.a))

    def _solve_zero(self):
        return (-self.b) / (2 * self.a)

    def _solve_im(self):
        re = (-self.b) / (2 * self.a)
        im = sqrt(abs(self.D)) / (2 * self.a)
        return (re, im)
