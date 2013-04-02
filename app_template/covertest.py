#! /usr/bin/env python
from fussy import nbio

def main():
    nbio.Process( 'coverage erase' )()
    nbio.Process( 'coverage run $(which django-admin.py) test {{app_name}}' )()
    nbio.Process( 'coverage report -m --include="*{{app_name}}*"')()

if __name__ == "__main__":
    main()

