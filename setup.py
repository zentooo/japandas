# -*- coding: utf-8 -*-
#!/usr/bin/env python

import codecs
import os
from setuptools import setup, find_packages

PACKAGE = 'japandas'
README = 'README.rst'
REQUIREMENTS = 'requirements.txt'

VERSION = '0.6.0.dev0'

def read(fname):
  # file must be read as utf-8 in py3 to avoid to be bytes
  return codecs.open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()

def write_version_py(filename=None):
    cnt = """\
version = '%s'
"""
    a = open(filename, 'w')
    try:
        a.write(cnt % VERSION)
    finally:
        a.close()

version_file = os.path.join(os.path.dirname(__file__), PACKAGE, 'version.py')
write_version_py(filename=version_file)

setup(name=PACKAGE,
      version=VERSION,
      description='pandas japanese extension',
      long_description=read(README),
      author='sinhrks',
      author_email='sinhrks@gmail.com',
      url='http://japandas.readthedocs.org/en/stable',
      license = 'BSD',
      packages=find_packages(),
      package_data = {'japandas.tseries': ['data/*.pkl']},
      install_requires=list(read(REQUIREMENTS).splitlines())
      )
