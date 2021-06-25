#!/usr/bin/env python3
import plistlib
import sys


def main(argv):
    with open(argv[1], 'rb') as fp:
        data = plistlib.load(fp)
        print(data)


if __name__ == '__main__':
    main(sys.argv)
