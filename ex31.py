# -*- coding:utf-8 -*-
print "You enter a dark room with two doors.Do you go to through door#1 or door #2?"
door = raw_input(">  ")

if door =="1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1.Take the cake."
	print "2.Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear =="1":
		print "The bear eats your face off.Good job."
	elif bear =="2":
		print "The bear eats your legs off."
	else:
		print "Well,doing %s is probably better. Better runs away." %bear
elif door =="2":
	print "You stare into the endless Cthulhu's retina."
	print "1. Blueberries."
	print "2.Yellow jacket clothespins."
	print "3.Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity =="1" or insanity =="2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
else: 
	print "Are you sure you don't want to make a good choice?"
	choice = raw_input("Choose again.         ")
	if choice == "1":
		print "Too late,but I still give you a way." #这里不知是否有更简便的方法？
		print "There's a giant bear here eating a cheese cake. What do you do?"
		print "1.Take the cake."
		print "2.Scream at the bear."
	
		bear = raw_input("> ")
	
		if bear =="1":
			print "The bear eats your face off.Good job."
		elif bear =="2":
			print "The bear eats your legs off."
		else:
			print "Well,doing %s is probably better. Better runs away." %bear
	else:
		print "You stumber around and fall on a knife and die. Good job!"

print "Let's play another game."
num = raw_input("give me a number.  ")
numm = float(num)

if numm < 0.:
	print "This is a negative."
elif numm in range(1,10):
	print "It's in the range of 1 to 10."
elif numm > 100:
	print "more than 100!"
else:
	print "Game over."