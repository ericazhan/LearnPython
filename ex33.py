#-*- coding:utf-8 -*-
i = 0
numbers = []

while i < 6:
	print "At the top i is %d" %i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ",numbers
	print "At the bottom i is %d" %i

	
print "The numbers:"

for num in numbers:
	print num

def numbering(numm):
	print "At the top i is %d" %numm
	numl = []
	numl.append(numm)
	print "Numbers now:",numl
	print "At the bottom i is %d" %numm	

	
i = 0
numbering(i)	
i += 1
numbering(i)
i += 1
numbering(i)
i += 1
numbering(i)
i += 1
numbering(i)
i += 1
numbering(i)

print "--------------------------------"
print "Now try a better way"
numll = []
def aa(sta,sto,incr):
	for nummm in range(sta,sto,incr):
		print "At the top i is %d" %nummm
		numll.append(nummm)
		print "Numbers now:",numll
		nummm = nummm + 1
		print "At the bottom i is %d" %nummm

aa(0,6,2)
	