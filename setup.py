from setuptools import setup

setup(
    name = 'gauge',
    version = '0.0.1',
    packages = ['lib/gauge'],
    entry_points = {
        'console_scripts': [
            'gauge = lib.gauge.__main__:main',
            'g = lib.gauge.__main__:main'
        ]
    }
)
