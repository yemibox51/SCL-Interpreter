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

with open('Documents/welcome.scl') as f:
	lines = f.readlines()

for line in lines:
    for word in line:
        if word == "/*":
            continue




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
print(lines)