#!/usr/bin/env python2.7

import sys

def grouper(n, items):
	group = []
	for i in items:
		group.append(i)
		if len(group) > n:
			yield group
			group = []
	if len(group) > 0:
		yield group

def is_palindrome(n):
	s = str(n)
	for i in range(0,(len(s) / 2)):
		a = s[i]
		b = s[-(i+1)]
		if a != b:
			return False
	return True

def digit_nums(min_val, max_val):
	for i in range(min_val, max_val+1):
		yield i

def reverse_digit_nums(min_val, max_val):
	l = list(digit_nums(min_val, max_val))
	l.reverse()
	for i in l:
		yield i

def palindromes(min_val, max_val):
	nums = reverse_digit_nums(min_val, max_val)
	nums = list(nums)

	res = None

	for i in nums:
		for j in nums:
			prod = i * j
			if is_palindrome(prod):
				yield prod

def largest_palindrome(min_val, max_val):
	all_pals = list(palindromes(min_val, max_val))
	return all_pals

lpal = list(largest_palindrome(100,999))
lpal.sort()

print "Largest:", lpal[-1]

