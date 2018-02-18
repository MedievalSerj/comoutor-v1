import unittest

from computor_v1.polynom.errors import format_error, format_position_indicator


class TestError(unittest.TestCase):

    def test_format_position_indicator(self):
        indicies = [0, 6]
        self.assertEqual(format_position_indicator(indicies, 7), '^     ^')
        tst_str = '5  * X^0'
        indicies = [1]
        self.assertEqual(format_position_indicator(indicies, len(tst_str)),
                         ' ^      ')
        tst_str = '5  * X^0'
        indicies = [7]
        self.assertEqual(format_position_indicator(indicies, len(tst_str)),
                         '       ^')

    def test_fomat_error(self):
        error_msg = 'Invalid input. to many spaces:'
        args = ('5  * X^0', ' ^      ')
        # print(format_error(error_msg, *args))
        self.assertEqual(format_error(error_msg, *args),
                         'computor: Invalid input. to many spaces:'
                         '\n5  * X^0'
                         '\n ^      ')
        error_msg = 'Invalid input'
        self.assertEqual(format_error(error_msg),
                         'computor: Invalid input')
