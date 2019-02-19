#!/usr/bin/env python3

# publish on pypi
# ---------------
#   $ python3 setup.py sdist
#   $ twine upload dist/imagecluster-x.y.z.tar.gz

import os, importlib
from setuptools import setup
from distutils.version import StrictVersion as Version

here = os.path.abspath(os.path.dirname(__file__))
bindir = 'bin'
with open(os.path.join(here, 'README.rst')) as fd:
    long_description = fd.read()

setup(
    name='imagecluster',
    version='0.2.0',
    description='cluster images based on image content using a pre-trained ' \
'deep neural network and hierarchical clustering',
    long_description=long_description,
    url='https://github.com/elcorto/imagecluster',
    author='Steve Schmerler',
    author_email='git@elcorto.com',
    license='BSD 3-Clause',
    keywords='image cluster vgg16 deep-learning',
    packages=['imagecluster'],
    install_requires=open('requirements.txt').read().splitlines(),
##    scripts=['{}/{}'.format(bindir, script) for script in os.listdir(bindir)]
)
