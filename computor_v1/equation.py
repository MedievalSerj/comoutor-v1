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
        res = re.findall('^([ 0-9.X^*+-]+)=([ 0-9.X^*+-]+)$',
                         self.equation_str)
        if len(res) != 1 or len(res[0]) != 2:
            raise InputError()
        self.left_side_str = res[0][0].strip()
        self.right_side_str = res[0][1].strip()

    def _extract_parts(self):
        left_side_extracted = re.findall('(([0-9.]*)[ ]*\*?)?[ ]*X(\^([012]))?',
                                        self.left_side_str)

        # print(left_side_extracted)
        left_side_extracted = [(0 if item[1] is '' else float(item[1]),
                               0 if item[3] is '' else int(item[3])) for item in
                               left_side_extracted]
        #
        print(left_side_extracted)
        # right_side_extracted = re.search('(([0-9.]*)[ ]*\*?)?[ ]*X(\^([012]))?',
        #                                  self.right_side_str)
        # right_side_extracted = [(-float(item[0]), int(item[1])) for item in
        #                         right_side_extracted]
        # self.equation.extend(left_side_extracted)
        # self.equation.extend(right_side_extracted)
