from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

ps = PorterStemmer()

f = open("input.txt",'r')

#example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

example_words = f.read()

sentence=[]
for w in example_words:
    sentence.append(lemmatizer.lemmatize(w))
   # print(ps.stem(w))


with open("output.txt","a") as f:
    print(sentence,file=f)
