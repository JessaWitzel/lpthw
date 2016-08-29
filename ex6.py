x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
#We are printing strings by using small variables
print x
print y
#reprinting that string within a new string. %r prints no matter what. %s makes sure it is a string?!
print "I said: %r." %x
print "I also said: '%s'." %y
#I have a question about this What does the %r do here?
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
#I don't get this either. I'm confused
print joke_evaluation % hilarious

w =  "This is the left side of..."
e = "a string with a right side."
#this is easy, print two stings by adding them together
print w + e