from sys import argv

script, user_name, color = argv
prompt = 'huh? '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, my boy {color}?")
likes = input(prompt)

print(f"Where do you live, {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"Is it {color}?")
yesorno = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
