import redis, redisbayes
rb = redisbayes.RedisBayes(redis=redis.Redis())
from sys import argv

script, normalfile, crazyfile = argv

with open(normalfile) as f:
    normallist = f.readlines()

with open(crazyfile) as f:
    crazylist = f.readlines()

for crazy in crazylist:
    rb.train('crazy', crazy)

for normal in normallist:
    rb.train('sane', normal)

print rb.classify('This show used to be brilliant. Not anymore.')

