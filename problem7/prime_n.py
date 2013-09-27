#!/usr/bin/env python2.7

from math import sqrt
import sys

#tgt = 100000000
tgt = 10001
#tgt = 1001
#tgt = 6

def is_prime(n, known_primes):
	sqr = int(sqrt(n))
	for i in known_primes:
		if i > sqr:
			break
		if n % i == 0:
			return False
	return True

def first_n_primes(n):
	count = 1
	known_primes = [2]

	pos = 3
	step = 2

	while count < n:
		if is_prime(pos, known_primes):
			yield pos
			known_primes.append(pos)
			count += 1

		pos = pos + 1

primes = list(first_n_primes(tgt))
primes = list(primes)
print "Last prime:", primes[-1]

