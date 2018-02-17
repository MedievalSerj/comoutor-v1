import click
from .equation import Equation


@click.command()
@click.argument('equation_str')
@click.option('-f', '--filename', default=None)
def run(filename, equation_str):
    """
    cli tool that solves simple polynomial equations
    """
    equation = Equation(equation_str)


if __name__ == '__main__':
    run()
