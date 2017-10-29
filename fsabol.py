#!/usr/bin/env python
import sys

def fix(source):
	newsource = []
	for s in source:
		s = s.lstrip(" ")
		if s=="": s="\n"
		newsource.append(s)
	return newsource

if __name__ == '__main__':
	if len(sys.argv)!=2:
		print "ERROR: wrong number of arguments.\nUsage: fsabol <filename>"
		exit(-1)
	filename = sys.argv[1]
	print "Fixing Spaces at the Beginning of Lines in file '%s'..." % (filename),
	with open(filename) as fi:
		source = fi.readlines()
	with open(filename, "w") as fo:
		fo.write("".join(fix(source)))
	print "DONE!"