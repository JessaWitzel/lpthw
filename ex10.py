tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list: 
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

she_said = "She said %r" % "'fuck' you" #double quote escape
we_said = "Once upon a time was 'once" #single quote escape but is this needed?
he_said = "\t hells \n NO"

print we_said
print she_said
print he_said
