import random
from urllib.request import urlopen
import ssl
import sys

#variable
WORD_URL = "https://learncodethehardway.org/words.txt"
#empty list
WORDS = []
#dictionary
PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and ***",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@",
    "*** = %%%()":
        "Set *** to an instance of class %%%",
    "***.***(@@@)":
        "From *** get the *** function, call it with parameter @@@",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'"
}

#do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False
#workaround that ignores SSL certificate failing
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#load up the words from the website
for word in urlopen(WORD_URL, context=ctx).readlines():
    WORDS.append(str(word.strip(), encoding = "utf-8"))
#function that takes 2 arguments
def convert(snippet, phrase):
    #variable assigned to capitalizing each word in WORDS
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    #variable assigned to random words
    other_names = random.sample(WORDS, snippet.count("***"))
    #open lists
    results = []
    param_names = []

    #for loop defined as 0 to # of snippets minus one
    for i in range(0, snippet.count("@@@")):
        #variable set as random integer 1 or 2
        param_count = random.randint(1,3)
        #appends param_names list with comman and string that joins one or two words together
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

    #for loop that loops twice. Treats snippet, phrase as it's own list.
    for sentence in snippet, phrase:
        #this is how you duplicate a list or string *not working
        result = sentence

        #fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        #fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        #fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        #append result onto results list
        results.append(result)

    return results

#keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
