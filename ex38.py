ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) !=10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one) #append stuff with the next_one
	print "There are %d items now." % len(stuff)
	
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1] #this is going to print the second item on the list
print stuff[-1] #print the last item on the list
print stuff.pop() #this is going to pop off the last item in the list
print ' '.join(stuff) #This joins the list into a string
print '#'.join(stuff[3:5]) #Joined item at 3 with item at 4 (stop at 5) with # in the middle