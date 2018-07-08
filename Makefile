package = computor_v1


install_dev:
	pip3 install --editable .

install:
	pip3 install .

install_user:
	pip3 install --user .

isort:
	isort -rc computor_v1

flake:
	flake8 $(package)

test:
	coverage run -m unittest discover $(package)
	coverage report -m

uninstall:
	pip3 uninstall computor_v1 -y

make clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -f `find . -type f -name '@*' `
	rm -f `find . -type f -name '#*#' `
	rm -f `find . -type f -name '*.orig' `
	rm -f `find . -type f -name '*.rej' `
	rm -f `find . -type f -name '*.egg-info' `
	rm -f .coverage
	rm -rf coverage
	rm -rf cover
	rm -rf htmlcov
	rm -rf .cache
	rm -rf .eggs
	rm -rf *.egg-info
	rm -rf .env
