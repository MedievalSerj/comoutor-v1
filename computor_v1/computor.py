#!/usr/bin/env python

import sys

from computor_v1.polynom import Equation, InputError, Solver


def run(equation_str):
    equation = Equation(equation_str)
    try:
        equation.validate_equation()
        equation.parse_equation()
    except InputError as e:
        print(str(e))
        sys.exit(0)
    equation.print_info()
    if not equation.validare_polynomial_degree():
        sys.exit(0)
    equation.fix_missing_degrees()
    solver = Solver(equation)
    solver.print_discriminant_msg()
    s = solver.solution()
    print(s)


def parse_args():
    usage = '''usage: computor.py [-h] equation_str

    positional arguments:
    equation_str  polynomial equation

    optional arguments:
        -h, --help    show this help message and exit'''
    if len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print(usage)
        sys.exit(0)
    return sys.argv[1]


def execute():
    equation_str = parse_args()
    run(equation_str)


if __name__ == '__main__':
    """
    cli tool that solves simple polynomial equations
    """
    execute()
