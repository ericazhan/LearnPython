from sys import argv

script,filename = argv

print "We're going to erase %r." %filename
print "If you don't want that,hit CTRL-C(^C)."
print "If you do want that,hit RETURN."

raw_input("?")

print "Opening the file.."
target = open(filename,"w")

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm goint to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm goint to write these to the file."


ff = "%s\n%s\n%s\n" %(line1,line2,line3)
target.write(ff)

print(type(ff))


#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally,we close it."
target.close()

ff = open(filename)
print ff.read()



