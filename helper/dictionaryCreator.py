""" This helper script builds the dictionary for number of words and their syllables """
import re
from collections import defaultdict
import pickle
import os.path

# Class Word
class Word:
	def __init__(self, word, syllables, rhyme):
		self.syllables = syllables
		self.rhyme = rhyme
		self.word = word

# Class RhymingDictionary
class RhymingDictionary:
	def __init__(self):
		if os.path.isfile("rhymingDictionary.p"):
			print "LOADED RHYMING DICTIONARY!!!"
			self.dictByWord = pickle.load( open( "rhymingDictionary.p", "rb" ) )
		else:
			# open the dictionary text file
			f = open('cmudict.0.7a.txt')

			# read the lines of the file
			lines = f.readlines()
			f.close()

			# create the dictionaries
			self.dictByWord = {}
			#dictByRhyme = defaultdict(list)
			#dictBySyllable = defaultdict(list)

			# for all the words in the dictionary (one per line), find stats and add them to corresponding dictionaries
			for str in lines:
				sections = re.split('[ ]', str)
				word = sections[0]

				rhyme = sections[-3] + " " + sections[-2] + " " + sections[-1]

				# the number of numbers indicates the number of syllables
				syllable = len ( filter(lambda x: x in '1234567890', list(str)) )
				
				w = Word(word, syllable, rhyme)
				self.dictByWord[word] = w
				#dictByRhyme[rhyme].append(w)
				#dictBySyllable[syllable].append(w)

			""" Print dictByWord
			for entry in dictByWord:
				print dictByWord[entry].word
				print dictByWord[entry].rhyme
			"""

			""" Print dictByRhyme
			for entry in dictByRhyme:
				table = dictByRhyme[entry]
				print "New Rhyme: " + entry
				for word in table:
					print word.word
			"""

			""" Print dictBySyllable
			for entry in dictBySyllable:
				table = dictBySyllable[entry]
				print "Syllable Count: " + entry
				for word in table:
					print word.word
			"""

			# write to pickle
			pickle.dump( self.dictByWord, open( "rhymingDictionary.p", "wb" ) )

	def getDictByWord(self):
		return self.dictByWord
	"""
	def getDictByRhyme():
		return dictByRhyme

	def getDictBySyllable():
		return dictBySyllable
	"""