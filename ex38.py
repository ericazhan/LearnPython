#-*- coding:utf-8 -*-
ten_things = "Apples Oranges Crows Telephon Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(" ") #新事物！
more_stuff = ["day","night","song","frisbee","corn","banana","girl","boy"]

while len(stuff)!=10:
	next_one = more_stuff.pop()
	print "Adding:",next_one
	stuff.append(next_one)
	print "There's %d intems now." %len(stuff)
	
print "There we go:",stuff
print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] ##这是啥？
print stuff.pop()
print ''.join(stuff) #这是啥？？
print '#'.join(stuff[3:5]) #这又是啥？？