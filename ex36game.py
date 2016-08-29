print """ It's a beautiful, sunny, fall day and you have gone for a walk to enjoy the weather. 
		Your headphones are in and you are jamming to your favorite playlist while breathing in fresh air.
		Everything seems right until...
		
			Suddenly.
			
				Out of nowhere.
				
					A masked man weilding a bloody knife jumps out of a blue van that was parked on the corner.
		
		He comes at you. You run to your right and straight through the slats of a metal fence that surround a big, fancy house.
		You've never been to this house, and it has a reputation for being inhabited by an oddball...
		but someone has to be in here that can help you right? 
		
		The front door is unlocked and you look over your shoulder to see the murderer still struggling to get through the gate. 
		You push open the door"""

def enterhouse():
	print """You enter a large living room with plush carpets, 
a spiral staircase, and a door to your left. There is a sleeping
dog guarding the staircase. Do you want to go into the room or up the stairs?"""
	
	movement= raw_input ("> ")
	
	if "door" or "left" or "room" in movement:
		print "You open the door and walk into a the dark room"
		clownroom()
	elif "stairs" or stair in movement:
		print "The dog wakes up and growls as you approach. He is going to attack. What do you do?"
		dogchoice = raw_input ("> ")
		dogmonster()
	else:
		print "You have to choose one! Quick, the murderer is coming and there is nowhere to hide in this room!"

def dogmonster():
	if "distract" in dogchoice:
		dead("The dog refuses to be distracted. He rips your face off.")
	elif "run" in dogchoice:
		dead("You run outside and the murderer immediately kills you.")
	elif "fight" or "kick" in dogchoice:
		print "You kick that dog's ass! Go you! It runs outside and the stairs are free."
		
	else:
		dead("That dog has a taste for blood. Your blood. You die a horrific bloody death.")
	
acceptable_words =["banana", "red", "bar"] 
		
def clownroom():
	print "Inside of the dark room sits a sad clown with an axe. He says 'You're going to have to make me laugh to get past'"
	print "Tell the sad clown your best joke."
	joke = raw_input("> ")
	joke = joke.lower()
	joke_words = joke.split(" ")
	if "knock" in joke:
		print "Who's there?"
		joke = raw_input("> ")
		print "That was great! I love knock knock jokes! You can pass into the kitchen."
		kitchen()
	elif "how many" in joke and "?" in joke:
		print "How many?"
		joke = raw_input("> ")
		print "Hahahaha! You can pass into the kitchen."
		kitchen()
	elif "why" in joke and "?" in joke:
		print "Why?"
		punchline = raw_input("> ")
		punchline = joke.split(" ")
		joke_words = punchline.lower().amend(joke_words)
	for word in joke_words:
		if word in acceptable_words:
			print "Hahaha, I love it! Go on into the kitchen. I will stall the murderer."
		else:
			dead("Wow, you are an awful joke teller. Time to die.")
	else:
		if "no" or "run" in joke:
			dead("The murderer, the dog, and the clown all converge on you. You die.")
		else: 
			dead("Wow, you are an awful joke teller. Time to die.")
	
		
def kitchen():
	print "The kitchen holds a ton of good weapons that you can use. "
	print "There is a butcher knife, a rolling pin, and an AK47 sitting on the countertop."
	print "There is also a huge monkey hanging from the pot rack."
	monkey_choice = raw_input("Do you want to ignore the monkey and grab a weapon or deal with the monkey?")
	if "ignore" in monkey_choice:
		weapon_choice = raw_input("Which weapon do you want?")
		print "The monkey tosses massive amounts of crap on you as you grab %s." %weapon_choice
		print "You are covered in poo but at least you have the %s. You head out the back door." %weapon_choice	
		outside()
	if "deal" in monkey_choice:
		print "You turn to the monkey, who is holding a handful of poo, and say 'Hey little dude.'"
		print "The monkey puts down his poo, wipes his hands on a kitchen town, and grabs your pant leg."
		print "The monkey leads you to safety."
		dead("You win!")
	else:
		dead("The monkey attacks you and bites your face off. You die.")	

def outside():
	print "You sneak alongside the house to the corner and look around"
	print "You see the murderer peeking into the clown room window. You use %s to get him right in the head." %weapon_choice		
	dead("He dies! You win!")
	
def dead(why):
	print why, "Good job!"
	exit(0)
	
enterhouse()