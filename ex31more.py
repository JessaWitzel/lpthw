print "Would you like to plant a garden?" 

start = raw_input ("> ")

if start == "yes":
	print "Would you like to plant vegetables, fruit, or a mixed garden?"
	garden = raw_input ("> ")
	
	if garden == "vegetables":
		print "Great, I love vegetables."
		print "What are your 3 favorite vegetables?"
		vegetables = raw_input ("> ")
		veg1, veg2, veg3 = vegetables.split(" ")
	
		print "Do you want to plant %s first?" %veg1
		yesno = raw_input (">")
		if yesno == "yes":
			print "Great, next we will plant %s and %s" % (veg2, veg3)
			
	elif garden == "fruit":
		print "Fruits are terrific!"
		print "What are your 3 favorite fruits?"
		fruits = raw_input ("> ")
		fruit1, fruit2, fruit3 = fruits.split(" ")
	
		print "Do you want to plant %s first?" %fruit1
		yesno = raw_input (">")
		if yesno == "yes":
			print "Great, next we will plant %s and %s" % (fruit2, fruit3)
	
	elif garden == "mixed":
		print "That's the kind of garden I would want too."
		print "What three things would you like to plant first?"
		plants = raw_input ("> ")
		plant1, plant2, plant3 = plants.split(" ")
	
		print "Do you want to plant %s first?" %plant1
		yesno = raw_input (">")
		if yesno == "yes":
			print "Great, next we will plant %s and %s" % (plant2, plant3)
		

elif start == "no":
	print "fuck you then"
	
