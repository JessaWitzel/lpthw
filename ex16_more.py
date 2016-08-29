from sys import argv

script, winefile = argv

txt = open (winefile)

print ("Here are the contents of your file %r.") %winefile
print txt.read ()
