try:
    from setuptool import setuptool
except ImportError:
    from distutils.core import setuptool

config = {
    'description': 'ex47 Test Case',
    'author': 'Rogier Schaap',
    'url' : 'URL to get it at',
    'download_url': 'Where to download it',
    'author_email': 'reschaap@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47',
}

setup(**config)