from setuptools import setup

setup(
    name='Kundaliya',
    version='0.1',
    packages=['kundaliya',],
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts': [
            'kund = kundaliya.__main__:main'
        ]
    },
)