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
		print 'This is pass block'
	print 'Current Letter:',ii
print "good bye!"


#break,except,import,print,class
for ii in 'python':
	if ii == 'h':
		print 'H commes!' #这句会打印出来，因为在break之前出现
		break
		print 'current one:' #这个不会被打印出来，break一出现，程序就断了
	print 'Current Letter:',ii
print 'goodbye'

for ii in 'python':
	if ii =='h':
		print 'H commes!'
		continue
		print 'will I appear?' #这句没有打印出来
	print 'Current Letter:',ii
print "good bye!"


#exec,in,raise,continue,finally
while True:
	value = raw_input("\nEnter a number:")
	
	if value == 'q':
		print "Exiting program."
		break
	if not value.isdigit():
		print "Enter digits only"
		continue
	value = int(value)
	print "Cube of ",value,"is",value**3