import unittest

from polynom import Equation
from polynom import InputError


class TestEquation(unittest.TestCase):

    def test_init(self):
        self.equation = Equation('5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0')
        self.assertEqual(self.equation.equation_str,
                         '5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0')

    def test_validate_allowed_characters(self):
        self.equation = Equation('5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0')
        self.assertEqual(self.equation._validate_allowed_characters(), None)
        self.equation = Equation('5 * e^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0')
        with self.assertRaises(InputError):
            self.equation._validate_allowed_characters()

    def test_validate_number_of_spaces(self):
        self.equation = Equation('5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0')
        self.assertEqual(self.equation._validate_number_of_spaces(), None)
        self.equation = Equation('5 *  X^0 + 4 * X^1    - 9.3 * X^2 = 1 * X^0')
        with self.assertRaises(InputError):
            self.equation._validate_number_of_spaces()

    def test_extract_sides(self):
        self.equation = Equation('5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0')
        self.equation._extract_sides()
        self.assertEqual(self.equation.left_side_str,
                         '5 * X^0 + 4 * X^1 - 9.3 * X^2')
        self.assertEqual(self.equation.right_side_str,
                         '1 * X^0')
        self.equation = Equation('5 * X^0 = + 4 * X^1 - 9.3 * X^2 = 1 * X^0')
        with self.assertRaises(InputError):
            self.equation._extract_sides()
        self.equation = Equation('5 * Y^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0')
        with self.assertRaises(InputError):
            self.equation._extract_sides()

    def test_extract_parts(self):
        self.equation = Equation('5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0')
        self.equation._extract_sides()
        self.equation._extract_parts()
        self.assertEqual(self.equation.equation,
                         [(5.0, 0), (4.0, 1), (-9.3, 2), (-1, 0)])
        self.equation = Equation('-X^0 - 4 * X^1 - 9.3 * X^ = - X')
        self.equation._extract_sides()
        self.equation._extract_parts()
        self.assertEqual(self.equation.equation,
                         [(-1, 0), (-4.0, 1), (-9.3, 1), (1, 1)])

    def test_parse_equation(self):
        self.equation = Equation('-X^0 - 4 * X^1 - 9.3 * X^ = - X')
        self.equation.parse_equation()
        self.assertEqual(self.equation.equation,
                         [(-1, 0), (-12.3, 1), (0, 2)])

    def test_reduce(self):
        self.equation = Equation('5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^3')
        self.equation.validate_equation()
        self.equation.parse_equation()
        self.equation._reduce()
        self.assertEqual(self.equation.equation,
                         [(5, 0), (4, 1), (-9.3, 2), (-1.0, 3)])
        self.assertEqual(self.equation.degree, 3)

    def test_fix_missing_degree(self):
        self.equation = Equation('-X^0 = 0')
        self.equation.validate_equation()
        self.equation.parse_equation()
        self.assertEqual(self.equation.equation,
                         [(-1, 0), (0, 1), (0, 2)])
        self.equation = Equation('X^1 = 0')
        self.equation.validate_equation()
        self.equation.parse_equation()
        self.assertEqual(self.equation.equation,
                         [(0, 0), (1, 1), (0, 2)])
        self.equation = Equation('-2X^2 = 0')
        self.equation.validate_equation()
        self.equation.parse_equation()
        self.assertEqual(self.equation.equation,
                         [(0, 0), (0, 1), (-2, 2)])

    def test_get_sign(self):
        self.assertEqual(Equation.get_sign(0, (-1, 0)), '')
        self.assertEqual(Equation.get_sign(1, (-1, 0)), '-')
        self.assertEqual(Equation.get_sign(1, (1, 0)), '+')

    def test_reduced_form(self):
        self.equation = Equation('5 * X^0 + 4 * X^1 = 1 * X^3')
        self.equation.validate_equation()
        self.equation.parse_equation()
        self.equation._reduce()
        self.assertEqual(self.equation.reduced_form,
                         '5.0 * X^0 + 4.0 * X^1 + 0 * X^2 - 1.0 * X^3 = 0')


if __name__ == '__main__':
    unittest.main()
