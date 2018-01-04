age = raw_input("How old are you?      ") 
#height = raw_input("How tall are you?")
#weight = raw_input("How much do you weigh?")

#print "So,you're %r old, %r tall and %r heavy." %(age,height,weight)

base = float(raw_input("Give me a base.            "       ))   #the space before " is the real space.
expo = int(float(raw_input("Give me a exponent."   )))
ans = base ** expo
print "So the answer for %d to the power %.2f is %.4f." %(base,expo,ans)