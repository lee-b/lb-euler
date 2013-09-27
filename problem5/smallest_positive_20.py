import sys

r = range(20,1,-1)
#r = range(10,1,-1)
print("Range is", r)

def positive_integers():
	for i in xrange(1,400000001):
		yield i

for i in positive_integers():
	ok = True
	for j in r:
		if i % j != 0:
			ok = False
			break

	if ok:
		print "FOUND: %d" % i
		sys.exit(0)

print "NOT FOUND"
sys.exit(20)

