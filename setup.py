#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
import os
import re
from setuptools import setup, find_packages


with open(os.path.join('pgwall_test', '__init__.py')) as ver_file:
    for line in ver_file:
        if line.startswith('__version__'):
            version=re.sub("'", "", line[line.index("'"):])

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['cellmaps_utils']

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Patrick Wall",
    author_email='pgwall@eng.ucsd.edu',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package with command line",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type = 'text/x-rst',
    include_package_data=True,
    keywords='pgwall_test',
    name='pgwall_test',
    packages=find_packages(include=['pgwall_test']),
    package_dir={'pgwall_test': 'pgwall_test'},
    scripts=[ 'pgwall_test/pgwall_testcmd.py'],
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/pgwall/pgwall_test',
    version=version,
    zip_safe=False)
