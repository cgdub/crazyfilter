import tbbay.py

script, normal, crazy = argv

normal = read(normal)
crazy = read(crazy)

normal = cleaner(normal)
crazy = cleaner(crazy)

normal, crazy = tokenize(normal, crazy)

bayes = train(normal, crazy)

print classify('Obama is literally Hitler', bayes)

