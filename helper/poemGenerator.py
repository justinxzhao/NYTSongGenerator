import re
import dictionaryCreator
from collections import defaultdict

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

def getPoem(lines):
	# create iotas of thoughts by split by: ,.;():
	iotas = []
	for str in lines:
		iotas.extend( re.split('[,.:;()"]', str) )

	# hash iotas by last word rhyme
	iotaRhymeDict = defaultdict(list)
	usedLastWords = defaultdict(list)
	for str in iotas:
		lastWord = re.split('[ ]', str)[-1].upper()
		if isInDictionary(lastWord):
			rhyme = dictByWord[lastWord].rhyme
		else:
			rhyme = "NULL"

		# check if the string already exists
		if str not in iotaRhymeDict[rhyme]:
			iotaRhymeDict[rhyme].append(str)
			usedLastWords

	"""
	# print out all the iotas by rhyme
	for rhyme in iotaRhymeDict:
		print "Rhyme: " + rhyme
		rhymeList = iotaRhymeDict[rhyme]
		for iota in rhymeList:
			print iota
			print ""
	"""

	# find rhyme schemes that have multiple iotas and build a string with rhyming pattern AABB
	str  = []
	for rhyme in iotaRhymeDict:
		if rhyme != 'NULL' and len( iotaRhymeDict[rhyme] ) >= 2:
			count = 0
			for iota in iotaRhymeDict[rhyme]:
				if count < 2:
					str.append(iota.upper())
					count = count+1

	return str