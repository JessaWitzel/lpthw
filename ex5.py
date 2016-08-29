name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180.00 #lbs
eyes = 'blue'
teeth = 'white'
hair = 'brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "That is %d centimeters tall." % (height * 2.54)
print "He's %d pounds heavy." % weight
print "That's %f kilograms heavy." % (weight * .4536)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)