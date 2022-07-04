import re
def detect_weight(text):
    weight_class= {   
        'kg': ['kg','kilogram', 'killogram', 'kiloggram', 'killoggram'], 
        'gm': ['gm','gram', 'grram', 'gramm'], 
        'ml': ['ml','mililiter', 'mililitter', 'milliliter', 'millilitter'], 
        'ltr': ['ltr','liter', 'lt', 'litter', 'litar', 'littar']
    }

    for key, values in weight_class.items():
        for value in values:
            if value in text:
                #if a weight class is found return the class and the weight
                return {'weight': re.search('^\d+', text).group(0),
                        'weight_class': key, 
                        'text': re.search('^\d+ *\w+', text).group(0)}
    
    #if nothing found return False
    return False
