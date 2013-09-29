import re
import dictionaryCreator
from collections import defaultdict

# word dictionary
dictByWord = dictionaryCreator.getDictByWord()

"""
def rhymesWith(word1, word2):
	w1 = dictByWord[word1]
	w2 = dictByWord[word2]
	if w1.rhyme != w2.rhyme:
		return 1
	else:
		return 0
"""

def getPoem(lines):
	# create iotas of thoughts by split by: ,.;():
	iotas = []
	for str in lines:
		iotas.extend( re.split('[:;]', str) )

	# hash iotas by last word rhyme
	iotaRhymeDict = defaultdict(list)
	usedLastWords = []
	for str in iotas:
		lastWord = re.split('[ ]', str)[-1].upper()
		if lastWord in dictByWord:
			# if the last word exists in our dictionary
			rhyme = dictByWord[lastWord].rhyme
		else:
			# otherwise, choose a null rhyme
			rhyme = "NULL"

		# check if the iota exists in iotaRhymeDict and that the lastWord hasn't been used yet
		if str not in iotaRhymeDict[rhyme] and lastWord not in usedLastWords:
			iotaRhymeDict[rhyme].append(str)
			usedLastWords.append(lastWord)

	"""
	# print out all the iotas by rhyme
	for rhyme in iotaRhymeDict:
		print "Rhyme: " + rhyme
		rhymeList = iotaRhymeDict[rhyme]
		for iota in rhymeList:
			print iota
			print ""
	"""

	# find rhyme schemes that have multiple iotas and build a string with rhyming pattern AABB...
	str  = []
	for rhyme in iotaRhymeDict:
		if rhyme != 'NULL' and len( iotaRhymeDict[rhyme] ) >= 2:
			count = 0
			for iota in iotaRhymeDict[rhyme]:
				if count < 2:
					str.append(iota.upper())
					count = count+1

	return str