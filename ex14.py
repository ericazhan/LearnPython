from sys import argv

script,user_name,date = argv
prompt = 'write your answer here please~                 '# both ' or '' will do.

print "Hi %s,I'm the %s script." %(user_name,script)
print "It's very nice to meet you in this special %s." %(date)
print "I'd like to ask you a few questions."
print "Do you like %s?" %user_name
#likes = raw_input(prompt)
likes = raw_input("just yes or no!         ")

print "Where do you live %s?" %user_name
lives = raw_input('prompt    ')     #in this way, prompt is no more a variable.

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright,so you said %r about liking me.
You live in %r,Not sure where that is.
And you have a %r computer. Nice.
""" %(likes,lives,computer)