# IMPORT ALL THE NECESSARY LIBRARIES
import nltk

#EXAMPLE TEXT CAN BE ANYTHING YOU WISH. IT CAN EVEN BE A TEXT FROM A FILE
EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."


#FUNCTION TO RUN THROUGH ALL THE WORDS IN EXAMPLE_TEXT AND FIND THE FREQUENCY OF ALL THE WORDS
frequency = nltk.FreqDist(EXAMPLE_TEXT) 
for key,val in frequency.items(): 
    print (str(key) + ':' + str(val))
