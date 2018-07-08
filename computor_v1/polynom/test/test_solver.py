import unittest

from computor_v1.polynom import Equation, Solver


class TestSolver(unittest.TestCase):

    def test_get_discriminant(self):
        equation = Equation('-1 * X^0 + 2 * X^1 + 3 * X^2 = 0')
        equation.fix_missing_degrees()
        self.solver = Solver(equation)
        self.assertEqual(self.solver.D, 0)

    def test_solve_positive(self):
        equation = Equation('-1 * X^0 + 2 * X^1 + 3 * X^2 = 0')
        equation.parse_equation()
        equation.fix_missing_degrees()
        self.solver = Solver(equation)
        solutions = self.solver._solve_positive()
        self.assertAlmostEqual(solutions[0], 0.3333333333333333)
        self.assertEqual(solutions[1], -1)

    def test_solve_zero(self):
        equation = Equation('9 * X^0 - 6 * X^1 + 1 * X^2 = 0')
        equation.parse_equation()
        equation.fix_missing_degrees()
        self.solver = Solver(equation)
        self.assertEqual(self.solver.D, 0)
        self.assertEqual(self.solver._solve_zero(), 3)

    def test_solution(self):
        equation = Equation('-1 * X^0 + 2 * X^1 + 3 * X^2 = 0')
        equation.parse_equation()
        equation.fix_missing_degrees()
        self.solver = Solver(equation)
        self.assertEqual(self.solver.solution(),
                         '0.333333\n-1')
        equation = Equation('9 * X^0 - 6 * X^1 + 1 * X^2 = 0')
        equation.parse_equation()
        equation.fix_missing_degrees()
        self.solver = Solver(equation)
        self.assertEqual(self.solver.solution(), '3')
        equation = Equation('7 * X^0 + 3 * X^1 + 5 * X^2 = 0')
        equation.parse_equation()
        equation.fix_missing_degrees()
        self.solver = Solver(equation)
        self.assertEqual(self.solver.solution(),
                         '-0.3 + j1.144552'
                         '\n-0.3 - j1.144552')


if __name__ == '__main__':
    unittest.main()
