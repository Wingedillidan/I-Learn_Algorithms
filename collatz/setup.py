try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'fastest way to conject',
    'author': 'Collin McLean',
    'url': 'http://github.com/wingedillidan/algorithms/collatz',
    'author_email': 'wingedillidan@gmail.com',
    'version': '1.5',
    'install_requires': ['nose'],
    'packages': ['collatz'],
    'scripts': [],
    'name': 'collatz'
}

setup(**config)
