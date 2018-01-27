#-*- coding:utf-8 -*-
goals = ["carrier","development","entertainment","finance","health","contribution","relationship"]

def plan(a):
	content = goals[a-1]
	print "The thing you want to do is of order %d, in the position %d." %(a,(a-1))

print "You have these choices for your next year."
print goals
choice = int(raw_input("What you want to do in the year 2018?          "))	
if choice in range(1,8):
	plan(choice)
else:
	print "You should give me a number from 1 to 6"
	
