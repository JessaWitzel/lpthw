from sys import argv #When you pass in a new argument to be used by argv you do it in the command line

script, user_name, watermelon= argv
prompt = '>' #what does this mean? Put in the prompt directly before it?

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions.", watermelon
print "Do you like me %s?" % user_name
likes = raw_input (prompt) #prompting with greater than symbol

print "Where do you live %ss?" % user_name #what I do if I want to add an s to what i get in the prompt?
lives = raw_input (prompt)

print "What kind of computer do you have?"
computer = raw_input (prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
