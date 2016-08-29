def chickens_and_ducks(chickens, ducks):
	print "You have %s chickens" % chickens
	print "You have %s ducks" % ducks
	print "You have %s poultry" % (chickens + ducks)
	
print "this is giving the function numbers directly"
chickens_and_ducks(23, 2)

print "This is using math"
chickens_and_ducks(16+6, 4-2)

print "This is using variables"
chickens = 22
ducks = 2
chickens_and_ducks(chickens, ducks)

print "This is using variables and math."
chickens_and_ducks(chickens +3 -3, ducks + 5 - 5)


chickens = raw_input("How many chickens do you have?")
ducks = raw_input("How many ducks do you have?")
chickens_and_ducks(int(chickens), int(ducks))

chickens_ducks = chickens_and_ducks
chickens_ducks(22,2)

