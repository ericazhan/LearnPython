#-*- coding:utf-8 -*-
#Learn 5 symbols each day 每天看5个
#20180203
#and,del,from,not,while

mylist = [1,2,3,4,5,6,7,8,7,6,5,4,3]
del mylist[4]
print mylist
del mylist
#print mylist

mylist = ["a","b","c","d"]
mylist.pop(0)
print mylist

#or,with,as,global,elif
def light():
	global aa  #make aa global
	aa = "life is beautiful."
	print aa

light()
print aa,"global keyword works!"

#assert,if,else,pass,yield
for ii in 'python':
	if ii =='h':
		pass
		#print 'This is pass block'
	print 'Current Letter:',ii
print "good bye!"


#break,except,import,print,class


#exec,in,raise,continue,finally