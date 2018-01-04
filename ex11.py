#print "How old are you?" #without comma, the cursor goes to next line.
#age = raw_input()
#print "How tall are you?",
#height = raw_input()
#print "How much do you weigh?",
#weight = raw_input()

#print "So,you're %r old,%r tall and %r heavy." %(age,height,weight)

print "Les't do some exponentiation."
print "Give me a base",
base = float(raw_input())
print "Give me then a exponent which is a integer.",
exponent = int(float(raw_input()))

ans = base ** exponent
print "So the answer for %.2f to the power %d is %.4f." % (base,exponent,ans)


#exponent = int(raw_input())  !wrong
#Line 20 doesn't work,because int() couldn't convert from string to number, but float() could.
