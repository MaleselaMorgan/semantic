import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

#when they compared cat and monkey the similarity was high since they have no similar letters.
#when they compared monkey and banana the similarity was close since they a letter n similar.
#when they compared cat and banana they were very close since they have 4 a in between them.

nlp2 = spacy.load('en_core_web_sm')
word4 = nlp2("cat")
word5 = nlp2("monkey")
word6 = nlp2("banana")
print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))

#when using ‘en_core_web_sm’ the similarity went up.

