from setuptools import setup, find_packages
from setuptools.command.install import install
import os

setup(
    name='cp-tool',
    version='1.0.0',
    packages=find_packages(),
    scripts=['cpt', 'cp-tool.py'],
    install_requires=[],
    description='CLI for creating competitive programming problem files',
    author='Simon Ashton',
    author_email='simonashton.dev@gmail.com',
    url='https://github.com/yourusername/cp-tool',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Linux',
    ],
)
