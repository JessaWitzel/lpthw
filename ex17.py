from sys import argv

script, from_file, to_file = argv

#we could do these two on one line, how?

indata = open(from_file).read()

open(to_file, 'w').write(indata)
