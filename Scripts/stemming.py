#IMPORTING THE NECESSARY LIBRARIES
from nltk.stem import PorterStemmer

#CALLING IN THE STEMMER
ps = PorterStemmer()

#DEFINING THE LIST OF WORDS TO BE STEMMED
example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

#PRINTING THE STEMMED WORDS ONE BY ONE
for w in example_words:
	print(ps.stem(w))

''' THERE ARE A LOT MANY STEMMERS AVAILABLE IN IN THE NLTK LIBRARY:
	1)PorterStemmer
	2)SnowballStemmer
	3)LancasterStemmer
	4)RegexpStemmer
	5)RSLPStemmer