from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import tahoma_api

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='tahoma_api',
    version=tahoma_api.__version__,
    url='http://github.com/philklei/tahoma-api/',
    license='Apache Software License',
    author='Philip Kleimeyer',
    install_requires=[],
    author_email='philip.kleimeyer@gmail.com',
    description='Tahoma Api - Python connect to Tahoma REST API',
    long_description=long_description,
    packages=['tahoma_api'],
    include_package_data=True,
    platforms='any'
)