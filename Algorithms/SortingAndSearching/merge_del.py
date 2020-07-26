class merge_del(object):
    """Reduce the array by deleting elements which are greater than all elements to its left
    using merge sort divide the array to left and right until the length is 1
    then when merging check if left array element is greater then right, if it is, append the right array element to the left array
    """
    def __init__(self,array):
       print( self.merge_del(array))      
             

    def merge(self,L, R):
        for i in R:
            if L[-1] > i:
                L = L + [i]
        return L

    def merge_del(self,l):
        if len(l) == 1:
            return l
        mid = int(len(l) / 2)
        L = l[:mid]
        R = l[mid:]       
        
        return self.merge(self.merge_del(L),self.merge_del(R))
            





