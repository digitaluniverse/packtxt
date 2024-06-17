from setuptools import setup, find_packages

setup(
    name='packtxt',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'packtxt=packtxt.cli:main',
        ],
    },
    install_requires=[
        # List dependencies here
    ],
)