
class sort:
    'A collection of well-known sorting algorithms, coded by @braddeibert. Includes: Selection sort, Insertion sort, Bubble sort, Merge sort, Quick sort. (.help() for more info)'
    
    def __init__(self):
        print('Classic sorting library imported. \n')
    
    # Complexity: O(n^2) time, O(1) space
    @staticmethod
    def selection(list):
        for i in range(len(list)):          #iterate each index i in unsorted list
            j = i
            min = list[i]
        
            
            for j in range(j, len(list)):   #find the minimum element in sublist from j: (j=i)
                if (list[j] < min):
                    oldMin = min
                    min = list[j]
                    list[j] = oldMin
            
            list[i] = min                   #place the jth smallest element in its correct position
            
            
    # Complexity: O(n^2) time, O(1) space
    @staticmethod
    def insertion(list):
        for i in range(len(list)):          #iterate each index i in unsorted list
            
            for j in range(i, 0, -1):       #iterate elements prior to i
                
                if (list[j] < list[j-1]):   #move element j back, if is less than element j-1
                    temp = list[j-1]
                    list[j-1] = list[j]
                    list[j] = temp
                else:
                    break                   #skip subsequent iterations, all elements prior to are sorted
                    
                    
    # Complexity: O(n^2) time, O(1) space
    @staticmethod
    def bubble(list):
        sorted = 0
        while (sorted != 1):                #iterate until the array is sorted
            sorted = 1
            
            for i in range(1, len(list)):   #iterate from 1 to list length
                
                if (list[i] < list[i-1]):   #swap element pair i & i-1 if they are out of order
                    sorted = 0              #array was unsorted, iterate again
                    
                    temp = list[i]
                    list[i] = list[i-1]
                    list[i-1] = temp
            
                  
    # Complexity: O(nlogn) time, O(n) space
    @staticmethod
    def merge(list):
        middle = int(len(list)/2)           #find midpoint for splitting into L/R halves
        left = list[:middle]
        right = list[middle:]
        
        if len(list) <= 1:
            return list
        else:                               #recursively sort both halves
            left = sort.merge(left)         
            right = sort.merge(right)       
            return sort._mergeParts(left, right)
    
    @staticmethod
    def _mergeParts(a, b):            #mergesort help function
        i, j = 0, 0
        aux = []
        
        #iterate through sublists a, b place smaller of a[i], b[j] into aux array
        while (j <= len(b) - 1 or i <= len(a) - 1):
            if (j == len(b)):
                aux.append(a[i])
                i += 1
            elif (i == len(a)):
                aux.append(b[j])
                j += 1
            elif (a[i] < b[j]):
                aux.append(a[i])
                i += 1
            else:
                aux.append(b[j])
                j += 1
                
        return aux
    
        
    #Complexity: O(nlogn) time, O(1) space
    @staticmethod
    def quick(list):
        if len(list) <= 1:
            return list
        
        #partition array on random pivot, recursively quicksort halves (not including pivot)
        sortedElement = sort._partition(list)   
        left = sort.quick(list[:sortedElement])
        right = sort.quick(list[sortedElement + 1:])
        return left + [list[sortedElement]] + right
        
    @staticmethod
    def _partition(list):             #quicksort help function
        import random
        random.shuffle(list)
        
        pivot = list[0]
        
        i = 1
        j = len(list) - 1
        
        #iterate i & j toward each other, swapping out of order elements
        while(i <= j):
            if list[i] < pivot:
                i += 1
            if list[j] >= pivot:
                j -= 1
            
            if (i < j): 
                swap = list[i]
                list[i] = list[j]
                list[j] = swap
        
        #swap pivot with element at j. pivot is now between all elements l.t. it, and g.t. it
        if (pivot >= list[j]):
            list[0] = list[j]
            list[j] = pivot
        
        return j
           
    def help():
        print(".selection(list) -- sorts input 'list', using selection sort.")
        print(".insertion(list) -- sorts input 'list', using insertion sort.")
        print(".bubble(list)    -- sorts input 'list', using bubble sort.")
        print(".merge(list)     -- sorts input 'list', using merge sort.")
        print(".quick(list)     -- sorts input 'list', using quick sort.")

        
    """
    MAIN FOR USER TESTING:
        arg 1: A list to be sorted
        arg 2: Algorithm with which to sort the list. 
            OPTIONS:
                1 - Selection Sort
                2 - Insertion Sort
                3 - Bubble Sort
                4 - Merge Sort
                5 - Quick Sort
    """
    def main(self, inArray, method):   
        
        print("\nUnsorted array:")
        print(inArray)                      #before
        
        if method == 1:
            sort.selection(inArray)
        elif method == 2:
            sort.insertion(inArray)
        elif method == 3:
            sort.bubble(inArray)
        elif method == 4:
            inArray = sort.merge(inArray)
        elif method == 5:
            inArray = sort.quick(inArray)
        else:
            print("\nMethod argument must be one of following: ")
            print("1 for selection")
            print("2 for insertion")
            print("3 for bubble")
            print("4 for merge")
            print("5 for quick")
        
        print("\nSorted array:")
        print(inArray)                      #after

