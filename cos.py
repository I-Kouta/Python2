# コサイン類似度
import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp("この文書を解析します")
for sent in doc.sents:
    for token in sent:
        print(
            token.i,
            token.text,
            token.vector,
            token.vector.shape,
        )
