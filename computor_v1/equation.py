import re


class Equation:
    def __init__(self, equation_str):
        self.equation_str = equation_str
        self.equation = []

    def parse_equation(self):
        re.findall('([0-9.]*)[ ]*\*[ ]*X\^([012])', self.equation_str)
