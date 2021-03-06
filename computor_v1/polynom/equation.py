import re
from re import finditer

from .errors import InputError, create_error


class Equation:
    def __init__(self, equation_str):
        self.equation_str = ' ' + equation_str
        self.msg = 'computor: '
        self.left_side_str = None
        self.right_side_str = None
        self.degree = 0
        self.equation = []

    def validate_equation(self):
        common_msg = 'Input error. All terms should be of "a * X^p" format:'
        self._validate_pattern('[^-0-9Xx^.+*= ]+',
                               'Input error. Invalid characters:')
        self._validate_pattern(' {2,}', 'Input error. To many spaces:')
        self._validate_pattern('\^-', 'Input error. Negative degree:')
        self._validate_pattern('X(?!\^)', common_msg)
        self._validate_pattern('(?<!x|X)\^', common_msg)
        self._validate_pattern('(x|X)\^(?![0-9]+)', common_msg)
        self._validate_pattern('(?i)\*(?! x|x)', common_msg)
        self._validate_pattern('(?i)(?<![0-9] |.[0-9])\*', common_msg)
        self._validate_pattern('(X|x)(X|x)', common_msg)

    def parse_equation(self):
        self._extract_sides()
        self._extract_parts()
        self._reduce()

    def print_info(self):
        print(f'Reduced form: {self.reduced_form}')
        print(f'Polynomial degree: {self.degree}')

    def validare_polynomial_degree(self):
        if self.degree > 2:
            print("The polynomial degree is stricly "
                  "greater than 2, I can't solve.")
            return False
        else:
            return True

    def _validate_pattern(self, pattern, message):
        error_index = []
        for item in finditer(pattern, self.equation_str):
            error_index.append(item.start())
        if error_index:
            error = create_error(
                message,
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

    def _extract_sides(self):
        res = re.findall('^([- 0-9.xX^*+]+)=([- 0-9.xX^*+]+)$',
                         self.equation_str)
        if len(res) != 1 or len(res[0]) != 2:
            raise InputError('Input error. Not a valid input')
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
            '(([-+]?)[ ]?([0-9.]*)[ ]*\*?)?[ ]*X(\^([0-9]+))?',
            side_str)
        return [((Equation._parse_factor(item[2], item[1])),
                1 if item[4] is '' else int(item[4])) for item in
                side_extracted]

    @staticmethod
    def get_sign(i, item):
        if i > 0 and item[0] >= 0:
            return '+'
        elif item[0] < 0 and i >= 0:
            return '-'
        else:
            return ''

    @property
    def reduced_form(self):
        res = ''
        for i, item in enumerate(self.equation):
            n = item[0]
            res += (f' {Equation.get_sign(i, item)}'
                    f'{abs(n) if not n.is_integer() else int(abs(n))}'
                    f' * X^{item[1]}')
        res += ' = 0'
        return res[1:]

    def _extract_parts(self):
        left_side_extracted = Equation._find_all(self.left_side_str)
        right_side_extracted = Equation._find_all(self.right_side_str)
        right_side_extracted = [(-item[0], item[1]) for item in
                                right_side_extracted]
        self.equation.extend(left_side_extracted)
        self.equation.extend(right_side_extracted)

    def _fix_missing_degre(self, degree):
        degrees = [item[1] for item in self.equation]
        if degree not in degrees:
            self.equation.append((0, degree))

    def fix_missing_degrees(self):
        self._fix_missing_degre(0)
        self._fix_missing_degre(1)
        self._fix_missing_degre(2)
        self.equation = sorted(self.equation,
                               key=lambda t: t[1])

    def _reduce(self):
        res = []
        self.equation = sorted(self.equation,
                               key=lambda t: t[1])
        for i, item in enumerate(self.equation):
            if not res:
                res.append(item)
            elif item[1] != res[-1][1]:
                res.append(item)
            else:
                res[-1] = (item[0] + res[-1][0], item[1])
        self.equation = res
        filtered_equation = list(filter(lambda x: x[0] != 0, self.equation))
        if filtered_equation:
            self.degree = max(filtered_equation, key=lambda x: x[1])[1]
