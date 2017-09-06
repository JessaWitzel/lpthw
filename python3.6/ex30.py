#setting variables
people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
#else if statement so if the first statement is false, it moves on.
elif cars < people:
    print("We should not take the cars.")
#else signals that if all other statements are not true, do this
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
