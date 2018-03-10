import click

from computor_v1.polynom import Equation
from computor_v1.polynom import InputError


@click.command()
@click.argument('equation_str')
@click.option('-f', '--filename', default=None)
def run(filename, equation_str):
    """
    cli tool that solves simple polynomial equations
    """
    equation = Equation(equation_str)
    try:
        equation.validate_equation()
        equation.parse_equation()
        equation.print_info()
        if not equation.validare_polynomial_degree():
            exit(0)
    except InputError as e:
        print(str(e))
        exit(0)


if __name__ == '__main__':
    run()
