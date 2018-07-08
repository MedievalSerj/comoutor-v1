from math import sqrt


class Solver:

    D_MESSAGE_POSITIVE = ('Discriminant is strictly positive,'
                          ' the two solutions are:')
    D_MESSAGE_ZERO = 'Discriminant is zero, the solution is:'
    D_MESSAGE_NEGATIVE = ('Discriminant is negative,'
                          ' the complex solutions are:')
    DEGREE_1 = 'The solution is:'

    def __init__(self, equation):
        self.equation = equation.equation
        self.degree = equation.degree
        self.a = self.equation[2][0]
        self.b = self.equation[1][0]
        self.c = self.equation[0][0]
        self.D = self._get_discriminant()

    def print_discriminant_msg(self):
        if self.degree == 1:
            msg = Solver.DEGREE_1
        elif self.degree == 0:
            return
        elif self.D > 0:
            msg = Solver.D_MESSAGE_POSITIVE
        elif self.D == 0:
            msg = Solver.D_MESSAGE_ZERO
        else:
            msg = Solver.D_MESSAGE_NEGATIVE
        print(msg)

    def solution(self):
        if (self.degree == 0 and self.equation[0][0] == 0
                and self.equation[1][0] == 0
                and self.equation[2][0] == 0):
            return 'All real numbers are solutions'
        elif self.degree == 0:
            return 'There are no solutions'
        elif self.degree == 1:
            return Solver._round_solution(self._solve_linear())
        elif self.D > 0:
            solution = self._solve_positive()
            return (f'{Solver._round_solution(solution[0])}\n'
                    f'{Solver._round_solution(solution[1])}')
        elif self.D == 0:
            solution = self._solve_zero()
            return f'{Solver._round_solution(solution)}'
        else:
            solution = self._solve_im()
            im_1, im_2 = Solver._get_im_parts(solution[1])
            return f'{Solver._round_solution(solution[0])} {im_1}\n' \
                   f'{Solver._round_solution(solution[0])} {im_2}'

    @staticmethod
    def _round_solution(number, precision=6):
        res = round(number, precision)
        return int(res) if res.is_integer() else res

    @staticmethod
    def _get_im_parts(im):
        im_1, im_2 = '', ''
        if im > 0:
            im_1 = '+ j' + str(Solver._round_solution(im))
            im_2 = '- j' + str(Solver._round_solution(im))
        elif im < 0:
            im_1 = '- j' + str(abs(Solver._round_solution(im)))
            im_2 = '+ j' + str(abs(Solver._round_solution(im)))
        return im_1, im_2

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
