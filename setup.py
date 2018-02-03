from setuptools import setup, find_packages


packages = find_packages()
description = 'cli tool that solves simple polynomial equations'
author = 'Serhii Ladonia'
author_email = 'ladonya.s@gmail.com'
url = 'https://github.com/MedievalSerj/comoutor-v1'


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='computor-v1',
    version='0.1',
    description=description,
    long_description=description,
    author=author,
    author_email=author_email,
    maintainer=author,
    maintainer_email=author_email,
    url=url,
    license='GPL',
    install_requires=requirements,
    packages=packages,
    test_suite='computor_v1.test',
    entry_points={
        'console_scripts': ['computor=computor_v1.main:run'],
    }
)
