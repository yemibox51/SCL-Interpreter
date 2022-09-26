# [x] Read a text file
	# [x] Accept a text file
	# [x] Strip the eveyrthing of white space except if is between ""
# [x] Keywords ?
# [] Identifiers 
# [] Values
# [] Operators
# [] Constants
# [] Special Characters

keywords = {"import", "function", "use", "symbol", "forward", "interface", "struct", "structype", "return", "array", "count", "integer", "short", "real", "float", "double", "tbool", "char", "tstring", "tbyte", "enum", "global", "variables", "define", "persistent", "shared", "static", "mextern", "mfile", "identifier", "pointer", "char", "mvoid", "double", "long", "value"}

classifiers = {"define", "import"}

words = []
word = ""

keywords_found = []
classifiers_found = []
identifiers_found = []

with open('Documents/welcome.scl') as f:
	lines = f.readlines()

comment_stack = []

for line in lines:
    """
    Skips Multi-Line Comments
    """
    if(line.find("/*") != -1):
        comment_stack.append("/*")
    elif(line.find("*/") != -1):
        comment_stack.pop()
        continue
    
    # No comments
    if(len(comment_stack) <= 0):
        words.append(line.split(" "))



    """
    # No comments
    if(len(comment_stack) <= 0):
        for letter in line:
            if letter == " ":
                if word in keywords:
                    keywords_found.append(word)
                elif word in classifiers:
                    classifiers_found.append(word)
                    for id in range(letter, len(len))

            word += letter
        print(line)
    """




"""
for letter in lines:
    if word == "/*":


	# if the letter has white space or new line, add the word to list
	if letter == " " or letter == "\n":
		words.append(word)
		word = ""
	else:
		word += letter
"""
# strip every line with \n
# strip everything to just the words
# if things have qoutation marks, need to be treated as the object itself

# print(words)
# print(lines)