import os
import sys
from .cqlshmain import main as cqlsh_main
from .cqlshmain import read_options

def main():
    cqlsh_main(sys.argv[1:], "")

if __name__ == '__main__':
    sys.exit(main()) 
