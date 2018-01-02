formatter = "%s %s %r %r"

print formatter %(1,2,3,4)
print formatter %("one","two","three","four")
print formatter %(True,False,False,True) #the 1st letter must be captital.
print formatter %(formatter,formatter,formatter,formatter)
print formatter %(
          " I had this thing.",
		  "That you could type up right.",
		  "But it didn't sing.",
		  "So I said goodnight."
		  )
		 
print '"double quotes?"'
print "'double quotes? '"

#try inputing a chinese character, not work. even after #, the program doesn't work.