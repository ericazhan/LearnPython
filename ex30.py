# -*- coding:utf-8 -*-
people = 30
cars = 40
buses = 15

if cars > people: #每一个if开启一个分支。这条路有三个岔口
	print "We should take the cars."
elif (cars > people) is True: #elif，表示和上边的if是在一个岔路口。
	print "We should not take the cars." 
else:
	print "We can't decide."
	
if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."
	
if people > buses: #这条路只有两个岔口
	print "Alright, lets' just take the buses."
else:
	print "Fine,let's stay home then."
	

	