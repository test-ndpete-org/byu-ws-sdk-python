#!/usr/bin/env python2.7

from distutils.core import setup
import sys
import subprocess

if sys.version_info < (2, 7, 0) or sys.version_info >= (3, 0, 0):
    sys.stderr.write("byu-ws-sdk-python currently requires Python 2.7.\n")
    sys.exit(-1)

# pypi requires reStructuredText and github requires Markdown, so we convert like so
# requires http://johnmacfarlane.net/pandoc/
# pandoc --from=markdown --to=rst --output=README.rst README.md

with open('README.rst') as rm_file:
    long_description = rm_file.read()

setup(name='byu-ws-sdk-python',
      version='0.9.3',
      description='A Python SDK for calling BYU REST web services.',
      long_description=long_description,
      author='Paul Eden',
      author_email='paul_eden@byu.edu',
      url='https://github.com/byu-oit-core-appeng/byu-ws-sdk-python',
      packages=['byu_ws_sdk'],
      data_files=[('', ['README.md', 'README.rst', 'LICENSE'])],
      license="MIT",
      requires=['requests (>=0.14.1, <=0.14.2)', 'simplejson', 'decorator']
      )
