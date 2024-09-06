#!/usr/bin/env python3

import os
import sys

from cqlshlib.cqlshmain import main

CASSANDRA_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '.')

if __name__ == '__main__':
    main(sys.argv[1:], CASSANDRA_PATH)
