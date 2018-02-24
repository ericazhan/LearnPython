#-*- coding:utf-8 -*-
#creat a mapping of state to abbreviation
states = {
	'Oregon' : 'OR',
	'Florida':'FL',
	'California':'CA',
	'New York':'NY',
	'Michigan':'MI'
	}

#create a basic set of states and some cities in them
cities = {
	'CA':'San Francisco',
	'MI':'Detroit',
	'FL':'Jacksonville'
	}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print '-'*10
print "NY State has:",cities['NY']
print "OR State has:",cities['OR']

#print some states
print '-'*10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is:",states['Florida']

#do it by using the state then cities dict
print '-'*10
print "Michigan has:",cities[states['Michigan']]
print "Florida has:",cities[states['Florida']]

#print every state abbeviation
print '-'*10
for state,abbrev in states.items():
	print "%s is abbreviated %s" %(state,abbrev) #猜测python并不懂；变换顺序也可以运行？可以！python并不认识英文。

#print every city in state
print '-'*10
for city,abbre in cities.items():
	print "%s has the city %s" %(city,abbre)
	
#now do both at the same time
print '-'*10
for aa,bb in states.items():
	print "%s state is abbreviated %s and has city %s" %(
	aa,bb,cities[bb]) #变换顺序可以吗？可以。

print '-'*10
#safely get an abbreviation by state that might not be there
state = states.get('Texas',None)

if not state:    #这个表示 state不存在？
	print "Sorry,no Texas."

#get a city with a default values
city = cities.get('TX','Does Not Exist')
print "The city for the state 'TX' is %s" %city


	















































