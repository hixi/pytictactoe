from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

    setup(
        name='pytictactoe',
        version='0.5.0',
        description='A Tic-Tac-Toe playground for reinforcement learning.',
        long_description=readme,
        author='Samuel Kurath',
        author_email='samuel.kurath@gmail.com',
        url='https://github.com/Murthy10/pytictactoe',
        license='MIT',
        packages=find_packages(exclude=('tests', 'docs')),
        scripts=['bin/pytictactoe'],
    )
