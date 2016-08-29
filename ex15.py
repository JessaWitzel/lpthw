from sys import argv #import the feature argv from the python library

script, filename = argv #establishes script and filename as arguments

txt = open (filename) #creates variable text that opens a file

print "Here's your file %r:" %filename #prints a string, inserts filename
print txt.read() #prints the results of the function, open the file and read it

print "Type the filename again:" #prints a string
file_again = raw_input(">") #requests raw input and assigns it to variable file_again

txt_again = open(file_again)#can't I just say print file_again.read?
#assigns variable txt_again to open file_again (function)
print txt_again.read() #prints the results of the function that opens the file and reads it