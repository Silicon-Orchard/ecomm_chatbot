import nltk
import spacy
from nltk import word_tokenize
from nltk import StanfordTagger
nlp = spacy.load("en_core_web_sm")

def find_product(text):
    keys = []
    tokens = word_tokenize(text)
    tags = nltk.pos_tag(tokens)
    print(tags)
    parsed_text = nlp(u"{}".format(text))
    
    subject = ""
    for tag in tags:
        if tag[1] == "NN" or tag[1] == "NNS":
            keys.append(tag[0])
    
    for text in parsed_text:
        if text.dep_ == "nsubj":
            subject = text.orth_
    if subject:
        keys.remove(subject)
    return keys