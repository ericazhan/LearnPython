#-*- coding:utf-8 -*-
#To design a game
#1. 设计这个游戏，画一张游戏地图
#2.列出所有学过的代码，复习一遍；
#3.敲代码，敲一段，运行一段，找错，再继续下一段；
#4.完成

from sys import exit
from os.path import exists

def left_1():
	print "you just came to the no one land."
	exit(0)
	
def left_2():
	print "There's a possibility to go back to the portail,do you want to seize it? "
	seize = raw_input("y or n?\n>")
	if seize == "y":
			print "Ok,you get what you want."
			#go to start
			start()
	elif seize == "n":
			print "You are brave,man.Then as you wish, you go to next room."
			#go to right_0
			right_0()
	else:
			print "I don't know what you want. "
			#exit(0)

def left_0():
	
	print "In front of you, there're two doors 1 and 2. You choose?"
	print """\t*1\n\t*2
	"""
	leftt = raw_input(">")
	if "1" in leftt:
		left_1()
	elif "2" in leftt:
		left_2()
	else:
		print "I don't know what you want."
	
		
def right_3():
	print "Give me a word with lenth more than 7"
	wordd = raw_input(">")
	if len(wordd) > 7:
		print "YOU WIN!"
		exit(0)
	else:
		print "Pity,just one more effort.."
		exit(0)

def right_2():
		
	goals = ["carrier","development","entertainment","finance","health","contribution","relationship"]
	print "Now it's new year!Do you make your goals?"
	print "You have 7 different goal:"
	for i in goals:
		print "\n\t* %s" %i #如果没错的话，这行=下一行内容
		#print "\n1 carrier\n2 development\n 3entertainment\n4 finance\n5 health\n6 contribution\n7 relationship"
		
	def plan(a):
		content = goals[a-1]
		print "The thing you want to do is of order %d, in the position %d." %(a,(a-1))
		print "The thing you want to do most is %r" %content
	
	while True:
		goal1 = raw_input("What you want to do the most in the year 2018?          ")
		
		if goal1.isdigit() is True:
			goal11 = int(goal1)
			if goal11 in range(1,8):
				plan(goal11)
				print "-------------"
				print "Don't forget what you want to do in 2018!"
				print "You are about to win! But not yet~"
				right_3()
			else:
				print "You should give me a number from 1 to 7"
		else:
			print "Man, learn to type a number."
			#回到上一个分支
			
			
def right_1():
	print "This is the maze!"
	left_2()


def right_0():
	print 'First thing: you are exactly in the "right" way !'
	print "But it's not easy to win the game!"
	
	while True:
		add1 =raw_input("3+2=? \n>")
		if add1 == "5":
			print "You could now choose among the 3 doors, 1,2,3:"
			rdoor = raw_input(">")
			while True:
				if rdoor == "1":
					right_1()
				elif rdoor == "2":
					right_2()
				elif rdoor == "3":
					right_3()
				else:
					print "You keep typing,keep typing."	
					
			
		else:
			print "Really?Are you kidding me?"
			
			
	



def start():
	print "Welcome to the 2018 lalaland!"
	print "You are in the starting point. Are you ready to choose the doors in front of you?"
	print """
	---------left-------------right--------
	---------right-------------left--------
	choose one!
	"""
	next =raw_input(">")
	
	if next == "left":
		left_0()
	elif next == "right":
		right_0()
	else:
		print "You stumble around the room until you starve."
		

start()
