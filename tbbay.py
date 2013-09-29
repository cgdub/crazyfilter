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

def tokenize(normal, crazy):
#    incoming = sys.argv[1]
#    incoming_crazy = sys.argv[2]
#    normal = TextBlob(read(incoming))
#    crazy = TextBlob(read(incoming_crazy))
    return normal.sentences, crazy.sentences



def train(normal, crazy):
    train = []
    for sentences in normal:
        train += (sentences, 'pos')
    for sentences in crazy:
        train += (sentences, 'neg')
    bayes = NaiveBayesClassifier(train)
    return bayes

def classify(new_comment, bayes):
    '''accepts string'''
    analyze = TextBlob(new_comment,classifier = bayes)
    return analyze.classify()
