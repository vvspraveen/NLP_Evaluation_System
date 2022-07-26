import nltk
from gensim import corpora,models,similarities
import numpy as np
import gensim as gen
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.metrics.pairwise import cosine_similarity as sims

def simi():
    #document = get_object_or_404(Document, id=id)
    #place your testing text in ip
    ip = ['There is no doubt at all that the GDP is considered one of the important economic indicators of the country, but not many may now that it also affects the stock market also. Yes, you heard it right. If an economy is poor or in bad shape, then it is quite obvious that it will lead to the low profits for the companies. If the profits are low, then it will ultimately lead to a fall in the stock prices. One of the main concerns for the investors is the negative GDP growth, which is one of the main factors undertaken by the economists to analyze whether the economy is under recession or not.Hence, it is quite clear that a higher GDP is extremely important for the better functioning of Indian economy. To get the access of the GDP annual and quarterly data one can keep track on the economic calendar to keep an eye on latest GDP data.']
    avg_sims = []


    #place your original text in file_docs
    file_docs = ['There is no doubt at all that the GDP is considered one of the important economic indicators of the country, but not many may now that it also affects the stock market also. Yes, you heard it right. If an economy is poor or in bad shape, then it is quite obvious that it will lead to the low profits for the companies. If the profits are low, then it will ultimately lead to a fall in the stock prices. One of the main concerns for the investors is the negative GDP growth, which is one of the main factors undertaken by the economists to analyze whether the economy is under recession or not.Hence, it is quite clear that a higher GDP is extremely important for the better functioning of Indian economy. To get the access of the GDP annual and quarterly data one can keep track on the economic calendar to keep an eye on latest GDP data.']
    checker=[]
    file2_docs=[]
    mx=[]

    tokens = sent_tokenize(file_docs[0])
    for line in tokens:
        checker.append(line)
            
    length_doc1 = len(checker)

    gen_docs = [[w.lower() for w in word_tokenize(text)] 
                for text in checker]

    dictionary = gen.corpora.Dictionary(gen_docs)
    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
    tf_idf = gen.models.TfidfModel(corpus)
    #find similarity module arguments, before there was a dirctory name
    sims = gen.similarities.Similarity(None,tf_idf[corpus],num_features=len(dictionary))

    tokens = sent_tokenize(ip[0])
    for line in tokens:
        file2_docs.append(line)
            
    for line in file2_docs:
        query_doc = [w.lower() for w in word_tokenize(line)]
        query_doc_bow = dictionary.doc2bow(query_doc)
        query_doc_tf_idf = tf_idf[query_doc_bow]
        m=max(sims[query_doc_tf_idf])
        #print(m)
        mx.append(m)

        #print('Comparing Result:\n', sims[query_doc_tf_idf])
        sum_of_sims =(np.sum(sims[query_doc_tf_idf], dtype=np.float32))
        avg = sum_of_sims / len(file_docs)
        #print(f'\n avg: {sum_of_sims / len(file_docs)}')
        avg_sims.append(avg)  
    print(mx)
    ag=sum(mx)/len(mx)
    print(ag)

simi()