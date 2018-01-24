# -*- coding: utf- 8 -*-
people = raw_input("the number of people?    ")
cats = 30
dogs = 15

if people < cats:
	print "Too many cats! The world is doomed!"
	
if people > cats:
	print "Not many cats! The world is saved!"
	
if people < dogs:
	print "The world is drooled on!"
	
if people > dogs:
	print "The world is dry!"
	
dogs +=5

if people >=dogs:
	print "People are greater than or equal to dogs."
	
if people <= dogs:
	print "People are less than or equal to dogs."
	
if people ==dogs:
	print "People are dogs."

if (cats > dogs) is True:
	print "The cats are greater than dogs."

if (cats > dogs) is False:
	print "Again the cats win!"