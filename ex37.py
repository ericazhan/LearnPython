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

class Rocket():
	def _init_(self):
		self.x=0
		self.y=0
		
	def move_up(self):
		self.y +=1

my_rocket = Rocket()
print my_rocket

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
	
def factorial(n):
    if  not isinstance(n, int):
        raise RuntimeError("Argument must be int")

    if n < 0:
        raise RuntimeError("Argument must be >= 0")

    f = 1
    for i in range(n):
        f *= n
        n -= 1

    return f

nn = int(raw_input("factorial/n>"))
factorial(nn)  #如果nn是整数，ok，不报错，但也不会出来任何东西，因为没有print命令。如果不是整数，报错，程序停止。

try:
    print("Factorial of 4 is:", factorial(4))
    print("Factorial of 12 is:", factorial("12"))
except RuntimeError:
    print("Invalid Input")
	

n = 5
# Test one.
if n == 5:
    print 'Yay ==!'

# Test two.
if n is 5:
    print 'Yay is!'
	
L = []
L.append(1)
if L == [1]:
    print 'Yay! == =='
# Holds true, but...

if L is [1]:
    print 'Yay! is is '
# Doesn't.

x = [1, 2, 3]
y = [1, 2, 3]
print x is y
print x == y

def addEm(x, y, z):
    #return x+y+z   
    print 'the answer is', x+y+z   #return表示方程的结束！在return后面的句子被忽略。
	
addEm(1,2,3)