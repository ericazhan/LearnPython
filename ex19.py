def cheese_and_crackers(cheese_count,boxes_of_crackers):
	print "you have %d cheeses!" %cheese_count
	print "You have %d boxes of crackers!" %boxes_of_crackers
	print "Man that's enough for a party!" 
	print "Get a blaket.\n"
#in the above part, we just DEFINE a function who can do print. But for the moment,no printing need to be done.	

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)


print "OR,we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)


print "We can even do math insed too:"
cheese_and_crackers(10+20,5+6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)

def luyanne(aa,bb,cc):
	print "I want to tell you the summation of these is %d." %(aa+bb+cc)
	print "I know the first number is %d." %aa
	print "the third number %d is good." %cc

print " ---------first------"	
luyanne(10,20,30)	

print " ---------second------"	
af = int(raw_input("could you give a integer number?          "))
luyanne (af,20,30)



print " ---------third------"	
luyanne(10+20,30,40*4)

print " ---------fourth------"	
rr = 10
tt = 20
gg = 30
luyanne(rr, tt, gg)

print " ---------fifth------"	
rrr = rr
ttt = tt
ggg = gg
luyanne(rrr,ttt,ggg)	

print " ---------sixth------"	
fff = float(raw_input("could you give a flottant number?          "))
luyanne (fff,20,30)

print " ---------seventh------"	
ee = fff + 30.20
luyanne (fff,ee,30)

print " ---------eighth------"	
luyanne (fff*10,ee,fff+ee)

print " ---------ninth------"	
luyanne (fff/ee,ee,fff+ee)

print " ---------tenth------"	
luyanne (fff*10,20,rrr)




