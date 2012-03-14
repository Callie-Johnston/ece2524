#!/usr/bin/env python

import re

def changeGrade(file, searchString, newGrade, verbose):
	for line in file:
		m = re.search(searchString, line)
		values = line.rstript().split(',')
		if m:
			if verbose:
				stderr.write("%r\n" % values)
			values[3] = newGrade
	print ",".join(values)

if __name__=='__main__':
	import fileinput
	from sys import stderr, stdout, argv, exit
	verbose = false
	if len(argv) != 3:
		stderr.write("Usage: change_grade.py STRING VALUE \n")
		exit (1)
	else:
		changeGrade(fileinput.input('-'), argv[1], argv[2], verbose)	
