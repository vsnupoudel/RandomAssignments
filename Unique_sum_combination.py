import itertools
import numpy as np
input = [3, 13, 15]

def combination_of_sums(N, X, Y):
    """ N: Number of transactions
        X: Minimum profit
        Y: Maximum profit
    """
    listof = list( range(X,Y+1) )
    co = itertools.combinations_with_replacement(listof, N)
    sums = [np.sum(tup) for tup in co]
    #print(sums)
    return len(sums)


    
print( combination_of_sums(3,13,15) )
