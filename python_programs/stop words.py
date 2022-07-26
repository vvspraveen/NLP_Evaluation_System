from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#example_sentence = "This is an example showing off stop word filtration."
f = open("input.txt",'r',encoding="utf-8")

stop_words =set(stopwords.words("english"))

#words = word_tokenize(example_sentence)
words = word_tokenize(f.read())
filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

#print(filtered_sentence)

with open("output.txt","a") as f:
    print(filtered_sentence,file=f)
