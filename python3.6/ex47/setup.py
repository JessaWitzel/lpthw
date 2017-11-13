try:
    from setuptools import setup
except ImportError:
    from distutils.core import setuptools

config = {
    'description' : 'My Project',
    'author' : 'Jessa Witzel',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'jessa@riotousliving.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'ex47': 'projectex47'
}

setup(**config)
