#!/usr/bin/env python
import sys
import argparse
import fileinput

parser = argparse.ArgumentParser()
parser.add_argument("--raw", "-r", help="Print raw data", action="store_true")
parser.add_argument('file', metavar='FILE', nargs='*', help='Read from file. Default STDIN')
parser.add_argument('--get', "-g", type=int, help="Print a specific shift")
args = parser.parse_args()

def do_caesar(data):
	for i in range(-254,254):
		flag = ''
		valueError = False
		for pixel in data:
			try:
				flag += chr(ord(pixel) + i)
			except:
				valueError = True
		if args.get:
			if args.get == i:
				print flag
		elif flag:
			if args.raw:
				print str(i) + " - " + repr(flag) + "\n"
			else:
				print str(i) + " - " + (flag) + "\n"


for line in fileinput.input(files=args.file if len(args.file) > 0 else ('-',)):
	do_caesar(line)
	exit()

