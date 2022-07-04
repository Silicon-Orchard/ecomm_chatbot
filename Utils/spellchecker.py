import numpy as np
def check_spell(keys=[], search=[]):
    scores = np.zeros(len(search))
    for key in keys:
        for i, s in enumerate(search):
            if key in s:
                scores[i] += 1
    
    results = np.argpartition(scores, -(np.count_nonzero(scores==max(scores))))[-(np.count_nonzero(scores==max(scores))):]
    return results
            