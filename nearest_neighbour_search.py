


def index(list1, n):
      if n > list1[-1] or n < list1[0]:
              return -1
        
      def   N(start=0,end=len(list1) - 1):
         
          if n <= list1[end] :
                  return end
          mid = (start + end) //2      
          if n <= list1[mid]:
             return  N(start, mid)
          else:
             return N(mid, end)
      return N()  
                  
       



def neighbour(list1, n):
      if n > list1[-1] or n < list1[0]:
              return -1
        
      def   N(start=0,end=len(list1) - 1):
         
          if n <= list1[end] :
                  return list1[end]
          mid = (start + end) //2      
          if n <= list1[mid]:
             return  N(start, mid)
          else:
             return N(mid, end)
      return N()  

    
