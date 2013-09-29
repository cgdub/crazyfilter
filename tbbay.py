from text.blob import TextBlob
import random
from text.classifiers import NaiveBayesClassifier
import sys
random.seed(1)
#assumed things are clean
def read(file_of_words):
    corpus_words = ""
    fileObject = open((file_of_words), 'r', 0)
    for i in fileObject.read():
        corpus_words += i
    return corpus_words

incoming = sys.argv[1]
incoming_crazy = sys.argv[2]
normal = TextBlob(read(incoming))
crazy = TextBlob(read(incoming_crazy))
normal.sentences
crazy.sentences

train = []
for sentences in normal:
    train += (sentences, 'pos')
for sentences in normal:
    train += (sentences, 'neg')

bayes = NaiveBayesClassifier(train)
