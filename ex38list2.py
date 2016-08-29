bedtimes = ["22:00", "23:00", "23:30", "00:00", "never"]

responsible_bedtime = bedtimes[0:4]
irresponsible_bedtime = bedtimes[-1]

age = raw_input("How old are you?")
age = int(age)

if age <= 22:
	print "You are so young. You can go to bed %s" %irresponsible_bedtime
else:
	print "Choose one of these bedtimes dude"
	responsible_bedtime = ", ".join(responsible_bedtime)
	print responsible_bedtime
	
