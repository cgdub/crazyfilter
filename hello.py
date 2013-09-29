import os
from flask import Flask

import redis, redisbayes
rb = redisbayes.RedisBayes(redis=redis.Redis())
from sys import argv

with open('sanecomments.txt') as f:
    normallist = f.readlines()

with open('nuttycomments.txt') as f:
    crazylist = f.readlines()

for crazy in crazylist:
    rb.train('crazy', crazy)

for normal in normallist:
    rb.train('sane', normal)

app = Flask(__name__)

@app.route('/')
def hello():
    return rb.classify('I agree with this opinion. He poses a very interesting argument.')

