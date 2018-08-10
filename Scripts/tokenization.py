# IMPORT ALL THE NECESSARY LIBRARIES
from nltk.tokenize import sent_tokenize, word_tokenize

#EXAMPLE TEXT CAN BE ANYTHING YOU WISH. IT CAN EVEN BE A TEXT FROM A FILE
EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

# THIS WILL PRODUCE TOKENIZED SENTENCES
tokened_sent = sent_tokenize(EXAMPLE_TEXT)
# THIS WILL PRODUCE TOKENIZED WORD LISTING
tokened_word = word_tokenize(EXAMPLE_TEXT)

#PRINTING THE RESULTS
print(tokened_sent)
print(tokened_word)