#IMPORTING NECESSARY LIBRARIES
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#THIS IS JUST A DUMMY TEXT THAT CAN BE ANYTHING. EVEN A TEXT FROM A FILE
example_sent = "This is a sample sentence, showing off the stop words filtration."

#STOP WORDS ARE PARTICULAR TO RESPECTIVE LANGUAGES(english, spanish, freanch et-cetra)
stop_words = set(stopwords.words('english'))

#TOKENIZING ALL THE WORDS FROM THE EXAMPLE TEXT
word_tokens = word_tokenize(example_sent)

#FILTERING ALL THE STOPWORDS FROM THE EXAMPLE TEXT USING LIST COMPREHENSION
filtered_sentence = [w for w in word_tokens if not in stop_words]

#PRINTING OUT THE RESULTED SENTENCE
print(filtered_sentence)