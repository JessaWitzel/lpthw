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
random.shuffle(keys)

def guess_vocab(txtfile, current):
    print(f"Your vocab word is {current}.")
    whatever = input("Please type your definition: ")
    print("Here is the definition we have on file:")
    print(txtfile[current])
    print("Did you answer correctly?")

def correct_or_naw(current):
    response = input("> ")
    if response == "no":
        print("That's too bad! We will retest you on this later.")
        keys.insert(0, current)
        print(keys)
    else:
        print("Great job! We won't test you on that again.")


def vocab(txtfile):
    while keys:
    #pop off tuple into a variable
        current = keys.pop()
        #print(f"Your vocab word is {current}.")
    #give the vocab word and request input for the definition
        #whatever = input("Please type your definition: ")
    #show the definition and asked if it matched
        #print("Here is the definition we have on file:")
        #print(txtfile[current])
        #print("Did you answer correctly?")
    #if yes, move to next one, if no .insert in beginning of list.
        #response = input("> ")
        #if response == "no":
            #print("That's too bad! We will retest you on this later.")
            #keys.insert(0, current)
            #print(keys)
        #else:
            #print("Great job! We won't test you on that again.")

def definitions(txtfile):
    while keys:
        current = keys.pop()
        print(f"Please give us the vocab word that matches this definitions: {txtfile[current]}")
        whatever = input("> ")
        print(f"The correct vocab word is: {current}")
        print("Did you answer correctly?")
        response = input("> ")
        if response == "no":
            print("That's too bad! We will retest you on this later.")
            keys.insert(0, current)
            print(keys)
        else:
            print("Great job! We won't test you on that again.")

def mixture(txtfile):
    #I want to be able to call the vocab and definitions function inside of this function
    #separate the call and response and input from the while loop in the functions?
    #then call that within each function?


def begin(choice):
    if choice == "vocab":
        print("Let's do this")
        vocab(txtfile)
    elif choice == "definitions":
        definitions(txtfile)
    elif "mixture" in choice:
        mixture(x)
    else:
        print("Please type 'vocab', 'definitions', or 'mixture'")
        choice = input("> ")
        begin(choice)

begin(choice)
