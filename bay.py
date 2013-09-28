#Not done, going home and am switching to textblob
from pandas import *
import numpy as np
import os
import re
from nltk import NaiveBayesClassifier
import nltk.classify
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
from collections import defaultdict

data_path = os.path.abspath(os.path.join('.','data'))
spam_path = os.path.join(data_path, 'idiot')
normal = os.path.join(data_path, 'normal')

def get_msgdir(path):
    '''
    reads all files from a directory into a list of strins
    '''
    filelist = os.listdir(path)
    filelist = filter(lambda x: x != 'cmds', filelist)
    all_msgs = [get_msg(os.path.join(path,f)) for f in filelist]

    return all_msgs

#spit out lists for file names
train_batshit_crazy = get_msgdir(spam_path)
train_normal = get_msgdir(normal)

def get_msg_words(msg, stopwords = []):
    msg = re.sub('<(.|\n)*?>', ' ', msg)
    msg = re.sub('&\w+;', ' ', msg)
    msg_words = set(wordpunct_tokenize(msg.replace('=\n','').lower()))
    msg_words = [w for w in msg_words if re.search('[a-zA-Z]', w) and len(w) > 1]
    return msg_words

sw = stopwords.words('english')
sw.extend(['ll','ve'])

def features_from_messages(messages, label, feature_extractor, **kwargs):
    features_labels = []
    for msg in messages:
        features = feature_extractor(msg, **kwargs)
        features_labels.append((features, label))
    return features_labels

def word_indicator(msg, **kwargs):
    features = defaultdict(list)
    msg_words = get_msg_words(msg, **kwargs)
    for w in msg_words:
        features[w] = True
    return features


