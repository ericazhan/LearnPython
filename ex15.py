from sys import argv #from the module sys,we take out the function "argv". 

script,filename = argv #the argv has 2 variables,named "script" and "filename"

txt = open(filename) #we put a file in a drawer called txt.

print "Here's your file %r: " %filename 
print txt.read()  # we want to read the thing in the txt drawer.


print "Let's try another file:"
file_2 = raw_input("> ")  

txt_2 = open(file_2)  #file_2 is the name of the file and txt_2 is the drawer.

print "I will show you the second file and then the first one."
print txt.read()
print txt_2.read()  #actually it just showed txt_2. I need another function to open multiple files.