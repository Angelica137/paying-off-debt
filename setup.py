#!/usr/bin/env python

from setuptools import setup, find_packages
import os

long_description = '''
This project is a problem st for MITx600
'''

version = "1.0.0"

requirements = [
]

if __name__ == '__main__':
    setup(
        name='python_unit_testing_in_docker',
        version=version,
        description='Pytest Configuration Example',
        long_description=long_description,
        author="Angelica137",
        packages=find_packages(
            exclude=[
                'tests',
            ],
            include=[
                'scripts',
                'utils'
            ],
        ),
        license='',
        install_requires=requirements,
        classifiers=[
            'Development Status :: 1 - Planning',
            'Framework :: ',
            'Intended Audience :: ',
            'Intended Audience :: ',
            'License :: OSI Approved :: ',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Topic :: Software Development',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
    )
