import re
from re import finditer
from functools import reduce

from .errors import (InputError, create_error, format_error,
                     format_position_indicator)


class Equation:
    def __init__(self, equation_str):
        self.equation_str = equation_str
        self.msg = 'computor: '
        self.left_side_str = None
        self.right_side_str = None
        self.degree = 0
        self.equation = []

    def _validate_allowed_characters(self):
        error_index = []
        for item in finditer('[^-0-9Xx^.+*= ]+', self.equation_str):
            error_index.append(item.start())
        if error_index:
            error = create_error(
                'Input error. Invalid characters:',
                error_index,
                self.equation_str
            )
            raise InputError(error)

    def _validate_number_of_spaces(self):
        error_index = []
        for item in finditer(' {2,}', self.equation_str):
            error_index.append(item.start())
        if error_index:
            error = create_error(
                'Input error. To many spaces:',
                error_index,
                self.equation_str
            )
            raise InputError(error)

    def _sub_validate_factor(self, pattern, error_index):
        regexp = re.compile(pattern)
        for item in regexp.finditer(self.equation_str):
            groups = item.groups()
            if groups[0]:
                error_index.append(item.start() + 1)

    def validate_equation(self):
        self._validate_allowed_characters()
        self._validate_number_of_spaces()
        # self._validate_factor()

    def _extract_sides(self):
        res = re.findall('^([- 0-9.X^*+]+)=([- 0-9.X^*+]+)$',
                         self.equation_str)
        if len(res) != 1 or len(res[0]) != 2:
            raise InputError('Input error. Not a valid input file')
        self.left_side_str = res[0][0].strip()
        self.right_side_str = res[0][1].strip()

    @staticmethod
    def _parse_factor(factor, sign):
        if factor is '' and sign is '-':
            return -1
        elif factor is '':
            return 1
        elif sign is '-':
            return -float(factor)
        else:
            return float(factor)

    @staticmethod
    def _find_all(side_str):
        side_extracted = re.findall(
            '(([-+]?)[ ]?([0-9.]*)[ ]*\*?)?[ ]*X(\^([012]))?',
            side_str)
        return [((Equation._parse_factor(item[2], item[1])),
                1 if item[4] is '' else int(item[4])) for item in
                side_extracted]

    def _extract_parts(self):
        left_side_extracted = Equation._find_all(self.left_side_str)
        right_side_extracted = Equation._find_all(self.right_side_str)
        right_side_extracted = [(-item[0], item[1]) for item in
                                right_side_extracted]
        self.equation.extend(left_side_extracted)
        self.equation.extend(right_side_extracted)

    def _reduce(self):
        self.equation = sorted(self.equation,
                               key=lambda t: t[1],
                               reverse=True)
        self.equation = reduce(lambda x, y: [x, y]
                               if x[1] != y[1]
                               else [(x[0] + y[0], x[1])],
                               self.equation)

    def parse_equation(self):
        self._extract_sides()
        self._extract_parts()
