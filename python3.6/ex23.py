import sys
#sets three command line arguments 
script, input_encoding, error = sys.argv

#defining a function called main that takes 3 arguments + self
def main(language_file, encoding, errors):
    #This reads the next line of the file.
    line = language_file.readline()
    #if statement asking if the line exists
    if line:
        #runs the next function and puts those arguments in
        print_line(line, encoding, errors)
        #looping through the function again
        return main(language_file, encoding, errors)
#defining a function that takes 3 arguments and self
def print_line(line, encoding, errors):
    #strips whitespace out of the string by default
    next_lang = line.strip()
    #turns a string into bytes, default utf-8
    raw_bytes = next_lang.encode(encoding, errors=errors)
    #turns the bites back into a string, now in the default codec
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    #print the encoded string, a string, and then the decoded string
    print(raw_bytes, "<===>", cooked_string)
#open file and sets default encoding to utf-8
languages = open("languages.txt", encoding="utf-8")
#runs main function using open file.
main(languages, input_encoding, error)
