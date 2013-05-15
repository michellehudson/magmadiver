# this imports argv module.
from sys import argv

# this tells which variables I want to import from argv.
script, filename = argv

# this makes a variable txt to do "open" (a function) to a filename that the user inputs.
txt = open(filename)

# this returns the file, names the filename, and prints it with the read variable. 
print "Here is your file %r:" % filename
print txt.read()

# This prompts the user to input the filename themselves and assigns the variable name "file_again" to that input.
print "Type the filename again:"
file_again = raw_input("> ")

# this does the same thing line 8 does, but with the other variables. 
txt_again = open(file_again)

# this prints the file.
print txt_again.read()