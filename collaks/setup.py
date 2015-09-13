try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'fastest way to conject',
    'author': 'Collin McLean',
    'url': 'http://github.com/wingedillidan/algorithms/collaks',
    'author_email': 'wingedillidan@gmail.com',
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['collaks'],
    'scripts': [],
    'name': 'collaks'
}

setup(**config)
