#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from glob import glob
from os.path import basename
from os.path import splitext
from setuptools import find_packages
from setuptools import setup


setup(
    name="bit_boolean_flags",
    version="2.0",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    # metadata for upload to PyPI
    author="Kiran AK",
    author_email="kiran.txt@gmail.com",
    description='Bit boolean flag wrapper, allows you to store flags inside a single number.',
    long_description="""
Bit boolean flag wrapper, allows you to store flags inside a single number. 
Each flag uses powers of two, and the number of flags you can store depends on the capacity of the numeric data type.
You can do combined and or operations on the flag as per your requirement, refer examples.
""",
    license="MIT",
    download_url="https://github.com/redocnib/BitBooleanFlags/archive/v1.0.tar.gz",
    keywords="bit flags, boolean bit flags",
    url='https://github.com/redocnib/BitBooleanFlags',
    platforms='Cross platform',
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
)