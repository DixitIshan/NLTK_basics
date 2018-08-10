#IMPORTING NECESSARY LIBRARIES
from nltk.corpus import wordnet

#CREATING AN EMPTY LIST TO APPEND THE RESULT IN IT
antonyms = []

#
for syn in wordnet.synsets("small"):
	for l in syn.lemmas():
		if l.antonyms():
			antonyms.append(l.antonyms()[0].name())

#PRINTING THE RESULTS
print(antonyms)