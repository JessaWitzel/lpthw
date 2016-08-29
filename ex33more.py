numbers = []

x = raw_input("What number do you want to end your loop at?")
x = int(x)

y = raw_input ("What increment would you like to increase by?")
y = int(y)

for i in range(0, x, y):
	print "At the top i is %d" %i
	numbers.append(i)
	
	print "Numbers now: ", numbers
	print "At the bottom i is %d" %i
	
print "The numbers:"


for num in numbers: print num