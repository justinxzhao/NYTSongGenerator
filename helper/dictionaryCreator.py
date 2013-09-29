""" This helper script builds the dictionary for number of words and their syllables """
import re

f = open('cmudict.0.7a.txt')

# read the lines of the file
lines = f.readlines()
f.close()

dictionary = {}
for str in lines:
	word = re.split('[ ]', str)[0]
	charArray = list(str)
	numSyllables = len ( filter(lambda x: x in '1234567890', charArray) )
	dictionary[word] = numSyllables

def getDictionary():
	return dictionary