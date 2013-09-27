#!/usr/bin/env python2.7

def sq_sum(n, m):
	sum = 0
	r = range(n, m)
	print "Range:", list(r)
	for i in r:
		sum += i
	return sum * sum

def sum_sq(n, m):
	sum = 0
	for i in range(n, m):
		sq = i*i
		sum += sq
	return sum

def sum_diff(n, m):
	sq_s = sq_sum(n,m)
	s_sq = sum_sq(n,m)
	return  sq_s - s_sq

diff = sum_diff(1,101)
print "Diff:", diff

	
