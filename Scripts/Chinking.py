'''CHINKING IS A WAY TO REMOVE A CHUNK FROM A CHUNK. THE CHUNK THAT REMOVED FROM A CHUNK IS YOUR CHINK.'''
#IMPORT NECESSARY LIBRARIES
import nltk
from nltk.corpus import state_union
# PUNKTSENTENCETOKENIZER IS A BUILT IN UNSUPERVISED MACHINE LEARNING TOKENIZER. COMES PRE-TRAINED AND IT IS TRAINABLE AS WELL
from nltk.tokenize import PunktSentenceTokenizer

#PARSING THE TRAINING DATA
train_text = state_union.raw('2005-GWBush.txt')
#PARSING THE TESTING DATA
sample_text = state_union.raw('2006-GWBush.txt')

#TRAINING THE TOKENIZER WITH THE TRAINING DATA
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

#SETTING UP THE TRAINED TOKENIZER WITH THE TESTING DATA SET
tokenized = custom_sent_tokenizer.tokenize(sample_text)

'''
REMOVING FROM THE CHINK ONE OR MORE VERBS, PREPOSITIONS, DETERMINERS, OR THE WORD 'to'
'''
def process_content():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            chunkGram = r"""Chunk: {<.*>+}
                                    }<VB.?|IN|DT|TO>+{"""

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

            chunked.draw()

    except Exception as e:
        print(str(e))

process_content()