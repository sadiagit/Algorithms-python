class merge_sort(object):
    """Implementation of merge sort"""

    def merge_sort(self, arr):
       if len(arr) >1: 
        mid = len(arr)//2 # Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        self.merge_sort(L) # Sorting the first half 
        self.merge_sort(R) # Sorting the second half 
  
        self.merge(L, R, arr)
             
    
    def merge(self, L, R, arr):
       i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
       while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
          
        # Checking if any element was left 
       while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
       while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1

    def __init__(self, array):
        self.merge_sort(array)
        i=0
        while i<len(array):
            print(array[i])
            i+=1