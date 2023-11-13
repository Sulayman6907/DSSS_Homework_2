from setuptools import setup, find_packages

setup(
    name='math-quiz',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here, if any
    ],
    entry_points={
        'console_scripts': [
            'math-quiz=math_quiz.main:math_quiz',
        ],
    },
)
