#!/usr/bin/env python
from setuptools import setup

readme_file = open('README.md', 'r')
long_description = readme_file.read()
readme_file.close()

with open('requirements.txt') as fp:
    install_requires = fp.readlines()

setup(
    name='tapeterm',
    version='0.2.1',
    author='Panagiotis Simakis',
    author_email='sp1thas@autistici.org',
    license='MIT',
    url='https://github.com/sp1thas/tapeterm',
    keywords=['kasetophono'],
    description='Listen kasetophono\'s playlists from your terminal',
    long_description=long_description,
    entry_points={'console_scripts': ['tapeterm = tapeterm.tapeterm:main']},
    install_requires=install_requires,
    packages=['tapeterm'],
    include_package_data=True
)
