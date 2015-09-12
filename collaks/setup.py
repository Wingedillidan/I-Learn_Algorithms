try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'fastest way to conject',
    'author': 'Collin McLean',
    'url': 'http://github.com/wingedillidan/algorithms/collaks',
    'author_email': 'wingedillidan@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'collaks'
}

setup(**config)
