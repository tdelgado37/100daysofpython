#! python
# madLibs.py - reads in text files and lets the user add their own
#   text anywhere the word ADJECTIVE, NOUN AND VERB appears in the file.
#   madLibs.py <filename> - loads in filename and will propt you
#       to replace keywords for your own

import sys

filename = sys.argv[1]
file = open(filename, 'r')
fileContent = file.read()

userAdjective = input("Please enter an adjective: ")

#get user verb
userVerb = input("Please enter a verb: ")

#get user noun
userNoun = input("Please enter a noun: ")

#replace the old key words for user defined ones in str
fileContent = fileContent.replace('ADJECTIVE', userAdjective)
fileContent = fileContent.replace('VERB', userVerb)
fileContent = fileContent.replace('NOUN', userNoun)


#write the new str to a new file
newFile = open('userFile.txt', 'w')
newFile.write(fileContent)

newFile.close()
file.close()
