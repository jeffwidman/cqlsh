import os
import sys
from .cqlshmain import main as cqlsh_main
from .cqlshmain import read_options

def main():
    cqlsh_main(*read_options(sys.argv[1:], os.environ))

if __name__ == '__main__':
    sys.exit(main()) 
