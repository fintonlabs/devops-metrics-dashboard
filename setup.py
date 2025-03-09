from setuptools import setup, find_packages

setup(
    name='github-metrics-dashboard',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests==2.25.1',
        'matplotlib==3.4.2',
        'pandas==1.2.4',
    ],
    entry_points={
        'console_scripts': [
            'github-metrics-dashboard=main:main',
        ],
    },
)