import unittest
from computor_v1.equation import Equation


class TestEquation(unittest.TestCase):

    def setUp(self):
        self.equation = Equation('5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0')

    def test_init(self):
        self.assertEqual(self.equation.equation_str,
                         '5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0')


if __name__ == '__main__':
    unittest.main()
