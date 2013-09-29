import os
import requests
import json
import urlparse
import math
from flask import Flask
from flask import render_template
import scrape

import redis, redisbayes
if not os.environ.get('REDISCLOUD_URL'):
    print "not heroku!"
    rb = redisbayes.RedisBayes(redis=redis.Redis())
else:
    url = urlparse.urlparse(os.environ.get('REDISCLOUD_URL'))
    rb = redisbayes.RedisBayes(redis=redis.Redis(host=url.hostname, port=url.port, password=url.password))
from sys import argv

with open('sanecomments.txt') as f:
    normallist = f.readlines()

with open('nuttycomments.txt') as f:
    crazylist = f.readlines()

for crazy in crazylist:
    rb.train('crazy', scrape.strip_tags(crazy)[0:300])

for normal in normallist:
    rb.train('sane', scrape.strip_tags(normal)[0:300])

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
    cs = getComments()
    commentlist = []
    for c in cs:
        cscraped = scrape.strip_tags(c)
        score = rb.score(cscraped)
        comment = {}
        comment['content'] = str(cscraped)
        comment['clf'] = str(rb.classify(cscraped)[0:300])
        if math.fabs(score['crazy'] - score['sane']) > 10:
            commentlist.append(comment)
    return render_template("index.html", commentlist=commentlist)

