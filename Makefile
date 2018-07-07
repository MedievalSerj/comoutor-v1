package = computor_v1


install_dev:
	pip install --editable .

install:
	pip install .

isort:
	isort -rc computor_v1

flake:
	flake8 $(package)

test:
	coverage run -m unittest discover $(package)
	coverage report -m

uninstall:
	pip uninstall computor_v1 -y
