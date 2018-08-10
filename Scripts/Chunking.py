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


#FUNCTION TO RUN THROUGH AND GROUP WORDS INTO MEANINGFUL CHUNKS
"""
<RB.?>* = "0 or more of any tense of adverb," followed by:
<VB.?>* = "0 or more of any tense of verb," followed by:
<NNP>+ = "One or more proper nouns," followed by
<NN>? = "zero or one singular noun."
"""
process_content()

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            print(chunked)
            
            #ITERATING THROUGH ALL THE SUBTREES AND FILTERING ONLY THE CHUNKS
            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                print(subtree)

            chunked.draw()

    except Exception as e:
        print(str(e))

process_content()
