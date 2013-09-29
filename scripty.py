import tbbay
from sys import argv

script, normal, crazy = argv

normal = tbbay.read(normal)
crazy = tbbay.read(crazy)

normal = tbbay.cleaner(normal)
crazy = tbbay.cleaner(crazy)

normal, crazy = tbbay.tokenize(normal, crazy)

bayes = tbbay.train(normal, crazy)

print tbbay.classify('Obama is literally Hitler', bayes)

