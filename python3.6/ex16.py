from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'r+')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ") + "\n"
line2 = input("line 2: ") + "\n"
line3 = input("line 3: ") + "\n"

print("I'm going to write these to the file.")

target.write(line1 + line2 + line3)

print("Now we'll read it.")
target.seek(0)
print(target.read())

print("And finally, we close it.")
target.close()
