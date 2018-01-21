# -*- coding: utf- 8 -*-
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmuly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
#above the \n will perform even in the """?

print "--------------------------"
print poem
print "-------------------------"

five = 10 - 2 + 3 -6
print "This should be five: %s" %five

def secret_formula(started):
	aa = started * 500
	bb = aa / 1000
	cc = bb / 100
	return aa,bb,cc
#as we can see above,方程里面的变量，随便命名，反正都是临时的名字，所以也因此后面的代码是不能用这些名字的
	

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." %secret_formula(50)	

begin = 50
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." %secret_formula(begin)	
	
start_point = 10000
beans,jars,crates = secret_formula(start_point)

print "With a starting point of %d" %start_point
print "We'd have %d beans, %d jars, and %d crates." %(beans,jars,crates)


















