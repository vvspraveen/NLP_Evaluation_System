import nltk
from nltk.tokenize import word_tokenize, sent_tokenize



sims = gensim.similarities.Similarity('C:/Users/rakesh/Desktop/PYTHON PROGRAMS PROJECT/',tf_idf[corpus],
                                        num_features=len(dictionary))


file2_docs = []

with open ('demofile2.txt') as f:
    tokens = sent_tokenize(f.read())
    for line in tokens:
        file2_docs.append(line)

print("Number of documents:",len(file2_docs))  
for line in file2_docs:
    query_doc = [w.lower() for w in word_tokenize(line)]
    query_doc_bow = dictionary.doc2bow(query_doc)


query_doc_tf_idf = tf_idf[query_doc_bow]
# print(document_number, document_similarity)
print('Comparing Result:', sims[query_doc_tf_idf]) 
