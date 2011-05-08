#!/usr/bin/env python

from distutils.core import setup

setup(name='pyed',
      version='0.1',
      description='An emacs like editor written in Python',
      author_email='pierre.depascale@gmail.com',
      author='Pierre De Pascale',
      package_dir={'pyed': 'src/pyed'},
      packages=['pyed'],
      scripts=['pyed']
     )
