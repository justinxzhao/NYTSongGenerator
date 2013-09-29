import re
import dictionaryCreator
from collections import defaultdict

# open the sample file
f = open('sample2.txt')

# word dictionary
dictByWord = dictionaryCreator.getDictByWord()

def isInDictionary(str):
	if str in dictByWord:
		return 1
	else:
		return 0

def rhymesWith(word1, word2):
	w1 = dictByWord[word1]
	w2 = dictByWord[word2]
	if w1.rhyme != w2.rhyme:
		return 1
	else:
		return 0

# read the lines of the file
lines = f.readlines()
f.close()

# create iotas of thoughts by split by: ,.;():
iotas = []
for str in lines:
	iotas.extend( re.split('[,.:;()]', str) )

# hash iotas by last word rhyme
iotaRhymeDict = defaultdict(list)
for str in iotas:
	lastWord = re.split('[ ]', str)[-1].upper()
	if isInDictionary(lastWord):
		rhyme = dictByWord[lastWord].rhyme
	else:
		rhyme = " "
	iotaRhymeDict[rhyme].append(str)

# print out all the iotas by rhyme
for rhyme in iotaRhymeDict:
	print "Rhyme: " + rhyme
	rhymeList = iotaRhymeDict[rhyme]
	for iota in rhymeList:
		print iota
	print ""

# find rhyme schemes that have multiple iotas and build a string with rhyming pattern AABB
str  = []
for rhyme in iotaRhymeDict:
	if rhyme != ' ' and len( iotaRhymeDict[rhyme] ) > 2:
		count = 0
		for iota in iotaRhymeDict[rhyme]:
			if count < 2:
				str.append(iota)
				count = count+1

# print out the poem
print "THE POEM!"
for item in str:
	print item.upper()