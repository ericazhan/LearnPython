#-*- coding:utf-8 -*-
from sys import exit

def gold_room(): #这个程序要倒着看。
	print "This room is full of gold.How much do you take?"
	
	next = raw_input(">")
	if next.isdigit() is True:
		how_much = int(next)
		if how_much in range(51):
			print "Nice,you're not greedy, you win!"
			exit(0)
		elif how_much > 50:
			dead("You greedy bastard!")
		else:
			print "OK.Game over."
	else:
		dead("Man,learn to type a number.") 
	#if "0" in next or "1" in next:
		#how_much = int(next)

		
#	if how_much < 50:
#		print "Nice,you're not greedy, you win!"
#		exit(0)
#	else:
#		dead("You greedy bastard!")
		
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False #??
	
	while True: #当以下的几个分支为True,就运行，一直运行。
		next = raw_input(">")
		
		if next =="take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next =="taunt bear" and not bear_moved: #嘲笑，辱骂
			print "The bear has moved from the door. yOu can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved: #先要把bear_moved转成True,这个分支才能进来。
			gold_room()
		else:
			print "I got no idea what that means."

def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He,it,whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	next = raw_input(">")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
		
def dead(why):
	print why,"Good job!"
	exit(0)
	
def start():
	print "you are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	next =raw_input(">")
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")
		
start() #这一步才真正有“外显内容”，之前全在自定义。