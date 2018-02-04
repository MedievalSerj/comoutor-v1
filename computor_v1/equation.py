import re
from .errors import InputError


class Equation:
    def __init__(self, equation_str):
        self.equation_str = equation_str
        self.left_side_str = None
        self.right_side_str = None
        self.equation = []

    def validate_equation(self):
        return True

    def _extract_sides(self):
        res = re.findall('^([- 0-9.X^*+]+)=([- 0-9.X^*+]+)$',
                         self.equation_str)
        if len(res) != 1 or len(res[0]) != 2:
            raise InputError()
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

    def parse_equation(self):
        self._extract_sides()
        self._extract_parts()
