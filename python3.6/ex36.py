#I don't want to write a game because I'm not that into video games.
#input text file as a command line argument
import random
vocab = {}

def create_vocab_dict():
    vocabtxt = open("examplevocab.txt")
    nextvocab = vocabtxt.readline().strip("\n")
    while nextvocab != "":
        #strip newline out of it

        key, value = nextvocab.split(", ", 1)
        vocab[key] = value
        print(vocab)
        nextvocab = vocabtxt.readline().strip("\n")

create_vocab_dict()

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
    input("Please type your definition: ")
    print("Here is the definition we have on file:")
    print(txtfile[current])
    print("Did you answer correctly?")

def guess_definitions(txtfile, current):
    print(f"Please give us the vocab word that matches this definition: {txtfile[current]}")
    input("> ")
    print(f"The correct vocab word is: {current}")
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
        current = keys.pop()
        guess_vocab(txtfile, current)
        correct_or_naw(current)

def definitions(txtfile):
    while keys:
        current = keys.pop()
        guess_definitions(txtfile, current)
        correct_or_naw(current)

def mixture(txtfile):
    while keys:
        current = keys.pop()
        guess_vocab(txtfile, current)
        correct_or_naw(current)
        if keys:
            current = keys.pop()
            guess_definitions(txtfile, current)
            correct_or_naw(current)

def begin(choice):
    if choice == "vocab":
        print("Let's do this")
        vocab(txtfile)
    elif choice == "definitions":
        definitions(txtfile)
    elif "mixture" in choice:
        mixture(txtfile)
    else:
        print("Please type 'vocab', 'definitions', or 'mixture'")
        choice = input("> ")
        begin(choice)

begin(choice)

#next, make it work with a comma separated txt file! How do I do that?
