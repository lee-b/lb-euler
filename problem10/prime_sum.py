#!/usr/bin/env python2.7

from math import sqrt

#limit = 10
limit = 2000000

def is_prime(n, primes):
	sq_n = sqrt(n)

	for p in primes:
		if p > sq_n:
			break

		if n % p == 0:
			return False

	return True

def primes_below(limit):
	primes = [2]
	yield primes[0]
	i = 3

	while i < limit:
		if is_prime(i, primes):
			primes.append(i)
			yield i

		i += 2

#primes = list(primes_below(limit))
#for p in primes:
#	print p

primes = primes_below(limit)
print "Sum:", sum(primes)

