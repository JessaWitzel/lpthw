#this defines cheese_and_crackers as the two variables and runs the function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"
#this prints a string	
print "We can just give the function numbers directly:"
#this calls the function and passes in the numbers
cheese_and_crackers(20, 30)

#this is the same but assigns the numbers a variable before passing in
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#also the same but includes math functions inside of the argument list
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
	