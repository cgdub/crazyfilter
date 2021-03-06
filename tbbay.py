from text.blob import TextBlob
import scrape
import random
from text.classifiers import NaiveBayesClassifier
import sys
#assumed things are clean
def read(file_of_words):
    '''Takes in a file and returns string'''
    corpus_words = ""
    fileObject = open((file_of_words), 'r', 0)
    for i in fileObject.read():
        corpus_words += i
    return corpus_words

def cleaner(string_of_words):
    '''takes in a string of words and removes html'''
    return scrape.strip_tags(string_of_words)

def tokenize(normal, crazy):
    '''returns tokenized versions of normal and crazy strings
    in that order'''
#    incoming = sys.argv[1]
#    incoming_crazy = sys.argv[2]
    normal = TextBlob(normal)
    crazy = TextBlob(crazy)
    return normal.sentences, crazy.sentences



def train(normal, crazy):
    '''takes tokenized normal and crazy, trains the bayes
    off of them, returns a trained bayes'''
    train = []
    #print normal.tokens
    for sentences in normal:
        train.append( (sentences, 'pos'))
    for sentences in crazy:
        train.append((sentences, 'neg'))
    random.seed(1)
    random.shuffle(train)
    bayes = NaiveBayesClassifier(train)
    return bayes

def classify(new_comment, bayes):
    '''takes a comment string (to be classified) and a trained bayes
    returns string 'pos' (normal) or 'neg' (crazy)'''
    analyze = TextBlob(new_comment,classifier = bayes)
    return analyze.classify()
