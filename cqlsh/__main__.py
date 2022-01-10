import os
import sys
from cqlsh.cqlsh import main as cqlsh_main
from cqlsh.cqlsh import read_options

def main():
    cqlsh_main(*read_options(sys.argv[1:], os.environ))

if __name__ == '__main__':
    sys.exit(main()) 
