#!/usr/bin/env python3
from math import *
import sys

tgt = 600851475143

res = None

def largest_factors(n):
	start = int(sqrt(n))
	end = 2
	step = -1

	if start % 2 == 0:
		start -= 1

	res = None

	for i in range (start, end, step):
		rem = n % i 
		if rem == 0:
			times = n / i
			res = i
			yield i

def is_prime(n):
	start = int(sqrt(n))
	end = 2
	step = -1
	for i in range(start, end, step):
		if n % i == 0:
			return False
	return True

def largest_prime(n):
	for i in largest_factors(n):
		if is_prime(i):
			return i

	return None

p = largest_prime(tgt)
if p is None:
	print "no primes found."
else:
	print "Largest prime factor: %d" % p



