#imports the argument feature from the system
from sys import argv
#identifies the arguments
script, input_file = argv

#create function  called print_all with argument f. Print the read of f.
def print_all(f):
	print f.read()
#create rewind function where reference point is the beginning of the file because it is set to 0	
def rewind(f):
	f.seek(0)
#create printaline function with two arguments. Then print one and reads one line from the other	
def print_a_line(line_count, f):
	print line_count, f.readline()
#variable currentfile is the open input file	
current_file = open(input_file)
#prints string
print "First let's print the whole file:\n"
#calls function print_all which reads and prints whole file
print_all(current_file)
#prints string
print "Now let's rewind, kind of like a tape."
#calls rewind function which goes to the beginning of the file I think
rewind(current_file)
#prints string
print "Let's print three lines:"
#prints current line, then one line of the file
current_line = 1
print_a_line(current_line, current_file)
#does that again but curser has moved to next line because we already read the first line
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
