print("What file would you like to read?")
filename = input(">")
txt = open(filename)

print(txt.read())

txt.close()
