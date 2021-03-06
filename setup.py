#!/usr/bin/env python
"""
=========
pyliquid-dsp
=========
"""
from setuptools import setup, find_packages

setup(
  name="pyliquid-dsp",
  version="0.0.1",
  packages=find_packages(exclude=['tests.*', 'tests', '.virt']),

  tests_require=['nose'],
  test_suite='nose.collector',

  author='Michel Pelletier',
  author_email='pelletier.michel@yahoo.com',
  description='liquid-dsp wrapper',
  long_description=__doc__,
  license='LGPL v3',
  url='https://github.com/michelp/pyliquid-dsp',
  install_requires=[
        'cffi',
        'docopt',
        ],
  entry_points = {
        'console_scripts' : [
            'freqdem = liquiddsp.tools.freqdem:main',
            ]
        },
)
