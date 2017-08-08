"""
Install TahomaApi
"""

from os.path import exists
from setuptools import setup, find_packages
import codecs
import os
import re

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name='tahoma_api',
    version=find_version('tahoma_api', '__init__.py'),
    url='http://github.com/philklei/tahoma-api/',
    license='Apache Software License',
    author='Philip Kleimeyer',
    install_requires=['requests>=2.0'],
    author_email='philip.kleimeyer@gmail.com',
    description='Tahoma Api - Python connect to Tahoma REST API',
    long_description=open('README.rst').read() if exists("README.rst") else "",
    packages=find_packages(),
    keywords='tahoma somfy io covers senors api',
    platforms='any'
)