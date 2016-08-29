statestocities = {
	'Florida': 'Miami', 
	'South Carolina': 'Clemson',
	'North Carolina': 'Raleigh',
	'Georgia': 'Atlanta',
	'Tennessee': 'Nashville'
}

florida_cities = ('Miami', 'Jacksonville', 'St. Petersburg')

statestocities['Virginia'] = raw_input("What is your favorite city in Virginia?")

statestocities['Florida'] = florida_cities

print statestocities
print "Our dictionary contains the states: ", statestocities.keys()

if 'Georgia' in statestocities:
	print "Georgia is in our dictionary."
else:
	print "Error."	