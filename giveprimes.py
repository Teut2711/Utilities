# Best Sieve Version(I just had this idea .I 'm not copying it from somewhere.I only understand Sieve of Eratosthenes at the moment.
                                  #It might already be a method.I just though of it .)

import numpy as np
from math import ceil, sqrt
from collections import deque



def primesupto(n):

             
        primesdone = deque([2])# at start putting 2 since it's the only even prime

        for i in range(3, n + 1, 2):  # only half of the numbers can be primes start from 3 reduces space complexity of Sieve of Eratosthenes
            t = min(range(len(primesdone)),key =lambda x: abs(sqrt(i)- primesdone[x]))## Only check till sqrt(nearest neighbour approch better)
            for j in range(t + 1):
                
                if i % primesdone[j] == 0:  break  #prime check from previously found primes

            else:
                primesdone.append(i)# add it
                
     

      
        return primesdone       
            
       


    
