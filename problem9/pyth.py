#!/usr/bin/env python2.7
from math import sqrt
import sys

def smaller_than(b):
	for a in range(1, b):
		yield a


def natural_numbers():
	i = 1
	while True:
		yield i
		i += 1

for c in natural_numbers():
	for b in smaller_than(c):
		for a in smaller_than(b):
			if a*a + b*b != c*c:
				# not a pythagorean triplet
				continue

			if a + b + c == 1000:
				print "Pythagorean triplet is", (a,b,c)
				print "Product is", a*b*c
				sys.exit(0)


print "Not found!"
