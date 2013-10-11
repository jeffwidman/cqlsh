#!/usr/bin/env python

from distutils.core import setup

setup(
    name='cqlsh',
    version='1.0.0',
    description=('A Python-based command-line client for running simple CQL commands on a Cassandra cluster'),
    keywords='python cql cassandra cqlsh',
    maintainer='Andrew Mussey',
    maintainer_email='admin@ajama.org',
    url='https://github.com/amussey/cqlsh',
    install_requires=[],
    packages=['cqlshlib'],
    scripts = [
        'cqlsh',
    ]
)
