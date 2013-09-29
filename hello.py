import os
import requests
import json
import urlparse
from flask import Flask

import redis, redisbayes
url = urlparse.urlparse(os.environ.get('REDISCLOUD_URL'))
rb = redisbayes.RedisBayes(redis=redis.Redis(host=url.hostname, port=url.port, password=url.password))
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

def getComments():
    res = requests.get("http://api.nytimes.com/svc/community/v2/comments/random.json?&api-key=5c80aa20d61dec8a332aea8ad7c7c0d7:3:68189777")
    entry = json.loads(json.dumps(res.json()))
    commentlist = []
    if entry.has_key("results"):
        if entry.get("results").has_key("comments"):
            for comment in entry.get("results").get("comments"):
                commentlist.append(comment.get("commentBody").encode('ascii', 'ignore'))
    return commentlist

@app.route('/')
def hello():
    comment = getComments()[0]
    result = str(comment) + "<br><br>" + str(rb.classify(comment))
    return result

