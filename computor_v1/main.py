import click
from .equation import Equation
from .errors import InputError


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
    except InputError as e:
        print(str(e))
        exit(0)
    print(equation.equation)
    print('Done')


if __name__ == '__main__':
    run()
