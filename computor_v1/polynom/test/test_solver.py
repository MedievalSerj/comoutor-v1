import unittest
from computor_v1.polynom import Solver


class TestSolver(unittest.TestCase):

    def test_get_discriminant(self):
        self.solver = Solver([(-1, 0), (2, 1), (3, 2)])
        self.assertEqual(self.solver.D,
                         16)

    def test_solve_positive(self):
        self.solver = Solver([(-1, 0), (2, 1), (3, 2)])
        solutions = self.solver._solve_positive()
        self.assertAlmostEqual(solutions[0],
                               0.333333333)
        self.assertEqual(solutions[1], -1)

    def test_solve_zero(self):
        self.solver = Solver([(9, 0), (-6, 1), (1, 2)])
        self.assertEqual(self.solver.D, 0)
        self.assertEqual(self.solver._solve_zero(), 3)

    def test_print_discriminant_msg(self):
        self.solver = Solver([(-1, 0), (2, 1), (3, 2)])
        self.assertEqual(self.solver.print_discriminant_msg(),
                         'Discriminant is strictly positive,'
                         ' the two solutions are:')
        self.solver = Solver([(9, 0), (-6, 1), (1, 2)])
        self.assertEqual(self.solver.print_discriminant_msg(),
                         'Discriminant is zero, the solution is:')
        self.solver.D = -5
        self.assertEqual(self.solver.print_discriminant_msg(),
                         'Discriminant is negative,'
                         ' the complex solutions are:')

    def test_solution(self):
        self.solver = Solver([(-1, 0), (2, 1), (3, 2)])
        self.assertEqual(self.solver.solution,
                         '0.3333333333333333\n-1.0')
        self.solver = Solver([(9, 0), (-6, 1), (1, 2)])
        self.assertEqual(self.solver.solution, '3.0')
        self.solver = Solver([(7, 0), (3, 1), (5, 2)])
        self.assertEqual(self.solver.solution,
                         '-0.3 + j1.1445523142259597'
                         '\n-0.3 - j1.1445523142259597')


if __name__ == '__main__':
    unittest.main()
