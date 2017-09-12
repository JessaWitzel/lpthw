#I don't want to write a game because I'm not that into video games.
#input text file as a command line argument
print("""Welcome to the vocab game!
    Would you like to be shown the vocab,
    the definitions, or a mixture of both?
    """)

choice = input("> ")

def vocab(file):
    print("We'll play")

def begin(choice):
    if choice == "vocab":
        x = "Hello"
        print("Let's do this")
        vocab(x)
    elif choice == "definitions":
        definitions(x)
    elif "mixture" in choice:
        mixture(x)
    else:
        print("Please type 'vocab', 'definitions', or 'mixture'")
        choice = input("> ")
        begin(choice)

begin(choice)
