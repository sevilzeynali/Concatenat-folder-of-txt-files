#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import unicode_literals

import io
import os
import sys
import argparse

parser = argparse.ArgumentParser(description=' This program concatenat all txt files of a directory in one txt file / each line is a file in the output file')
parser.add_argument('-d','--directory', help='directory of input files', type=str, required=False)
parser.add_argument('-o','--output', help='output txt file', type=str, required=False)
args = parser.parse_args()

if hasattr(args, 'directory'):
    if args.directory != None:
        DIRECTORY = args.directory

if not os.path.isdir(args.directory):
	print "Error : Input entered is not a directory"
	sys.exit(1)

if hasattr(args, 'output'):
    if args.output != None:
        OUTPUT = args.output

fWrite = io.open(OUTPUT, 'w', encoding='utf8')

data = ''
for filename in sorted(os.listdir(DIRECTORY)):
    path = os.path.join(DIRECTORY, filename)
    if os.path.isfile(path):
        with io.open(path, 'r', encoding='utf8', errors='ignore') as f:
            data += ' '.join(f.read().splitlines()) + '\n'

fWrite.write(data) 
fWrite.close()

