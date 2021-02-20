#!/usr/local/bin/python3

#  Convert bin to 1 binary file
#  Usage: convert_bin2bin.py <file>.bin

import os
import sys

hexLines = os.popen('convert_bin2hex ' + sys.argv[1]).read().splitlines()

for line in hexLines:
    print(bin(int(line, 16))[2:].zfill(32))
