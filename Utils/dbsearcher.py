import numpy as np
from ast import literal_eval
def searchdb(keys: list, keysen: list)->list:
    '''
    Searches the keysen list for avaible keys 
    '''
    scores = np.zeros(len(keysen))
    #Score the keysen items based on the kes that were provided as inputs
    for key in keys:
        for i, s in enumerate(keysen):
            if key in s:
                scores[i] += 1
    
    #get the indices containing max scores
    results = np.argpartition(scores, -(np.count_nonzero(scores==max(scores))))[-(np.count_nonzero(scores==max(scores))):]
    
    #Return the indices of the items in DB who has a match with keys
    return [i for i in results]