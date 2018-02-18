import unittest

from computor_v1.polynom.equation import Equation
from computor_v1.polynom.errors import InputError


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

    def test_validate_factor(self):
        self.equation = Equation('5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0')
        self.assertEqual(self.equation._validate_factor(), None)
        self.equation = Equation('5 * X^3 + 4 * X^1 - 9.3 * X^2 = 1 * X^5')
        with self.assertRaises(InputError):
            self.equation._validate_factor()
        self.equation = Equation('5 * X^00 + 4 * X^1 - 9.3 * X^2 = 1 * X^01')
        with self.assertRaises(InputError):
            self.equation._validate_factor()

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
                         [(-1, 0), (-4.0, 1), (-9.3, 1), (1, 1)])


if __name__ == '__main__':
    unittest.main()
