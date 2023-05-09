# コサイン類似度
import spacy
nlp = spacy.load('en_core_web_sm')
doc1 = nlp("ホントウのキミを知りたいの")
doc2 = nlp("ホントウのキミが知りたいの")
doc3 = nlp("僕らはそうマワルカガミ")

print(doc1. similarity(doc2))
print(doc2. similarity(doc3))
print(doc3. similarity(doc1))
