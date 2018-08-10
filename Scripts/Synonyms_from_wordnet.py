# IMPORT ALL THE NECESSARY LIBRARIES
from nltk.corpus import wordnet

#FINDING ALL THE SYNONYMS FROM THE CORPUS AND PRINTING THEM
synonyms = []
for syns in wordnet.synsets('here_goes_the_word_for_which_you_want_to_find_the_synonym_for'):
	synonyms.append(syns)

print synonyms


#FINDING ALL THE SYNONYMS FROM THE CORPUS AND THEIR LEMMAS PRINTING THEM
synonyms = []
for syn in wordnet.synsets('here_goes_the_word_for_which_you_want_to_find_the_synonym_for'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())

print(synonyms)