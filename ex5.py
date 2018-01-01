#my_name = 'Zed A.Shaw'
#my_age = 35 #not a lie
#my_height = 74 #inches
#my_weight = 180 #lbs
#my_eys = "blue"
#my_teeth = 'white'
#my_hair = 'Brown'

#print "let's talk about %s."% my_name
#print "He's %d inches tall." % my_height
#print "He's %d pounds heavy."%my_weight #the space after % is not necessary,but recommand.
#print "Actually that's not heavy."
#print "He's got %s eys and %s hair." % (my_eys,my_hair)  #the parenthesis() is necessary.
#print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky,try to get it exactly right
#print "If I add %d,%d,and %d I get %d." % (my_age,my_height,my_weight,my_age+my_height+my_weight)

name = 'luyanne'
age = 27 #not a lie
height = 74 #inches*2.54=cm
weight = 180 #lbs*0.4536 kg
eyes = "black"
teeth = 'white'
hair = 'black'

print "let's talk about %s." % name
print "let's talk about %r." % name
# print "let's talk about %d." % name    %d means interger, the variable is not a ingegral.
# print "let's talk about %f." % name    same reason 
print "She's %d inches tall,if you're not clear about inches, let's say %r cm" % (height,round(height*2.54) )
print "She's %d pounds heavy."% weight #the space after % is not necessary,but recommand.
print "Actually all above might not be true"
print "She's got %r eys and %s hair." % (eyes,hair)  

print "Her teeth are usually %s depending on the coffee." % teeth

#this line is tricky,try to get it exactly right
print "If I add %d,%d,and %d I get %d." % (age,height,weight,age+height+weight)