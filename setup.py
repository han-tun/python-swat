#!/usr/bin/env python
# encoding: utf-8
#
# Copyright SAS Institute
#
#  Licensed under the Apache License, Version 2.0 (the License);
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

''' Install the SAS Scripting Wrapper for Analytics Transfer (SWAT) module '''

import glob
from setuptools import setup, find_packages

try:
    README = open('README.rst', 'r').read()
except:
    README = 'See README.rst'

if glob.glob('swat/lib/*/tk*'):
    LICENSE = 'Apache v2.0 (SWAT) + SAS Additional Functionality (SAS TK)'
else:
    LICENSE = 'Apache v2.0'

setup(
    zip_safe=False,
    name='sas-swat',
    version='1.3.1-dev',
    description='SAS Scripting Wrapper for Analytics Transfer (SWAT)',
    long_description=README,
    author='SAS',
    author_email='Kevin.Smith@sas.com',
    url='http://github.com/sassoftware/python-swat/',
    license=LICENSE,
    packages=find_packages(),
    package_data={
        'swat': ['lib/*/*', 'tests/datasources/*'],
    },
    install_requires=[
        'pandas >= 0.16.0',
        'six >= 1.9.0',
        'requests',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
    ],
)
