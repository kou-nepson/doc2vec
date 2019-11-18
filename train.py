#coding: UTF-8
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

f = open('corpus.txt','r')

trainings = [TaggedDocument(words = data.split(),tags = [i]) for i,data in enumerate(f)]

#print(trainings)
print("学習中")
m = Doc2Vec(documents= trainings, dm = 1, vector_size=300, window=8, min_count=10, workers=4)
print("保存中")
m.save("model/doc2vec.model")
print(m.docvecs.most_similar(0))

#print(trainings)
