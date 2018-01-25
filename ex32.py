#-*- coding:utf-8 -*-
the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" %number

#same as above
for fruit in fruits:
	print "A fruit of type :%s" %fruit
	
#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in items
for i in change:
	print "I got %r" %i
	
#we can also build lists, first start with an ampty one
elements = []

#then use the range function to do 0 to 5 counts
for i in fruits:
	print "Adding %r to the list." %i
	#append is a function that lists understand
	elements.append(i)

#now we can print them out too
for i in elements:
	print "Element was:%r" %i

#drillout 2	
len_fruits = len(fruits)
for i in range(0,len_fruits):
	elements.append(i)
for i in range(0,len_fruits):
	print elements[i]
	
for i in range(5):
	a = i + 1
	print a
	
#-----这两个代码打印的结果很不一样!--------
for i in range(5):
    a = i + 1
print a




for i in range(2,20,5):
	a = i + 1
	print a
	
for i in range(99, 0, -1):
        if i == 1:
                print "1 bottle of beer on the wall, 1 bottle of beer!"
                print 'So take it down, pass it around, no more bottles of beer on the wall!'
        elif i == 2:
                print '2 more bottles of beer on the wall, 2 more bottles of beer!'
                print 'So take one down, pass it around, 1 more bottle of beer on the wall!'
        else:
                print "%r bottles of beer on the wall, %r bottles of beer!" %(i,i)
                print "So take it down, pass it around, %r more bottles of beer on the wall!" %(i-1)