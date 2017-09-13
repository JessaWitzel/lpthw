#I don't want to write a game because I'm not that into video games.
#input text file as a command line argument
import random

print("""Welcome to the vocab game!
    Would you like to be shown the vocab,
    the definitions, or a mixture of both?
    """)

choice = input("> ")
txtfile = {"word": "definition", "vocab": "iscool", "jessa": "isawesome"}
keys = list(txtfile.keys())
#randomize list of keys
random.shuffle(keys)
print(keys)

def vocab(txtfile):
    print("You got it.")
    #pop off tuple into a variable
    #give the vocab word and request input for the definition
    #show the definition and asked if it matched
    #if yes, move to next one, if no .amend back onto the list.

def begin(choice):
    if choice == "vocab":
        x = "Hello"
        print("Let's do this")
        vocab(txtfile)
    elif choice == "definitions":
        definitions(x)
    elif "mixture" in choice:
        mixture(x)
    else:
        print("Please type 'vocab', 'definitions', or 'mixture'")
        choice = input("> ")
        begin(choice)

begin(choice)
