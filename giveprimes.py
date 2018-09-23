
import collections

def sieve_eras(n):
      l = collections.deque( [False] * 2 + [True  for i in range(2, n + 1)] )

      k = 0

      while k <= n :
      
          while k<= n :
              if  l[k] == True:
                    yield k
                    break      
              k += 1

              
          j = k 
          while j <= n :
              l[j] = False
              j += k
              
          k += 1
              

##Junk for now
##def primesupto(n):
##
##             
##        primesdone = deque([2])# at start putting 2 since it's the only even prime
##
##        for i in range(3, n + 1, 2):  # only half of the numbers can be primes start from 3 reduces space complexity of Sieve of Eratosthenes
##            t = min(range(len(primesdone)),key =lambda x: abs(sqrt(i)- primesdone[x]))## Only check till sqrt(nearest neighbour approch better)
##            for j in range(t + 1):
##                
##                if i % primesdone[j] == 0:  break  #prime check from previously found primes
##
##            else:
##                primesdone.append(i)# add it
##        return primesdone       
 
