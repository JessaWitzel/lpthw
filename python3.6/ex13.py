from sys import argv

script, first, second, third = argv

print("This script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

color = input("What is your favorite color?")
food = input("What is your favorite food?")

print(f"""
    Mad libs style!
    We were walking down the {color} {first}
    when a vat full of {second} {food}
    came flying at us! We yelled {third}
    """)
