#-*- coding:utf-8 -*-
## Animal is-a object (yes,sort of confusing)look at the extra credit
class Animal(object):
	pass
	
##Dog is-a Animal
class Dog(Animal):
	def __init__(self,name):
	##From self get the name attribute and set it to name
	self.name = name
	
##define a class named cat is-a Animal(inherit from Animal)
class Cat(Animal):
	def __init__(self,name)；
	##
	self.name = name
	
##Person is-a object
class Person(object):
	def __init__(self,name):
	##
	self.name = name
	##person has-a pet of some kind
	self.pet = None

##
class Employee(Person):
	def __init__(self,name,salary):
	##just all names?
	super(Employee,self).__init__(name)
	##
	self.salary = salary
	
##
class Fish(object):
	pass
	
class Halibut(Fish):
	pass
	
rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank",12000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()