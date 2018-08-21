from setuptools import setup

setup(
    name = 'gauge',
    version = '0.0.1',
    packages = ['gauge'],
    entry_points = {
        'console_scripts': [
            'gauge = gauge.__main__:main'
        ]
    }
)
