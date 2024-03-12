from setuptools import setup

setup(
    name='pip-force',
    version='0.1',
    packages=['pip_force'],
    entry_points={
        'console_scripts': [
            'pip-force = pip_force.install:install_requirements',
        ],
    },
)