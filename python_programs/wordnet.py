from nltk.corpus import wordnet

syns = wordnet.synsets("estimate")

print(syns)

print(syns[0].lemmas()[0].name())

print(syns[0].definition())


w1 = wordnet.synset("compare.n.01")
w2 = wordnet.synset("estimate.n.01")

print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")

print(w1.wup_similarity(w2))


w1 = wordnet.synset("compare.n.01")
w2 = wordnet.synset("measure.n.01")

print(w1.wup_similarity(w2))
