import re
import dictionaryCreator

# open the sample file
f = open('sample.txt')

# read the lines of the file
lines = f.readlines()
f.close()

# create iotas split by: ,.;():
iotas = []
for str in lines:
	iotas.extend( re.split('[,.:;()]', str) )

def getVerse(size):
	count = 0
	while count < size:
		print iotas[count]
		print ""
		count += 1

	print "END VERSE"

getVerse(4)
dictionaryCreator.getDictionary()