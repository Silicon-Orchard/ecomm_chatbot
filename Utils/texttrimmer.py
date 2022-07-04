import re
from nltk.tokenize import word_tokenize
def trim(text):
    words = ["buy","verb","obtain","purchase","acquire","obtain","get",
            "pick","snap","take","secure","procure","score","have", "want"]
    
    prepositions = ["At","For","From","In","Into","Of","On","Over","To","With"]
    flag = False
    for buyword in words:
        if buyword in text:
            text = text[text.find(buyword):].replace(buyword, "")
            flag = True
            break
    if not flag:
        return False
    
    text = word_tokenize(text)
    for preposition in prepositions:
        if preposition in text:
            text.remove(preposition)
    text = " ".join(text)

    if 'and' in text:
        texts = text.split('and')
        return [text.strip() for text in texts]
    return [text.strip()]
    
