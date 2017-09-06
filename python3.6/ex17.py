from sys import argv
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")
indata = open(from_file).read()

out_file = open(to_file, 'w').write(indata)
print("Alright, all done.")

#when a file object goes out of scope Python closes it for you. It has not been saved anywhere as a file object.
