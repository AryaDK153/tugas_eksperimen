from math import floor, sqrt
import random

def bidirectional_conditional_insertion_sort(A = []):
    # Make Bidirectional-Conditional-Insertion-Sort Algorithm Here
    # A = Main Array

    'BCIS Functions'
    def SWAP(A = [], i = 0, j = 0):
        A[i], A[j] = A[j], A[i]
    def ISEQUAL(A = [], sl = 0, sr = 0):
        for k in range(sl+1, sr-1):
            if A[k] != A[sl]:
                SWAP(A, k, sl)
                return k
        return -1
    def INSRIGHT(A, item, sr, right):
        j = sr
        while j <= right and item > A[j]:
            A[j-1] = A[j]
            j += 1
        A[j-1] = item
    def INSLEFT(A, item, sl, left):
        j = sl
        while j >= left and item < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = item
    

    'BCIS Main Body'
    n = len(A)
    sorted_left = 0
    sorted_right = n-1

    while sorted_left < sorted_right:
        SWAP(A, sorted_right, sorted_left+((sorted_right-sorted_left)//2))
        if A[sorted_left] == A[sorted_right]:
            if ISEQUAL(A, sorted_left, sorted_right) == -1:
                return
        if A[sorted_left] > A[sorted_right]:
            SWAP(A, sorted_left, sorted_right)
        if (sorted_right-sorted_left) >= 100:
            for i in range(sorted_left+1, floor(sqrt(sorted_right-sorted_left))):
                if A[sorted_right] < A[i]:
                    SWAP(A, sorted_right, i)
                elif A[sorted_left] > A[i]:
                    SWAP(A, sorted_left, i)
        
        else:
            i = sorted_left+1
        lc = A[sorted_left]
        rc = A[sorted_right]
        while i < sorted_right:
            item = A[i]
            if item >= rc:
                A[i] = A[sorted_right-1]
                INSRIGHT(A, item, sorted_right, n-1)
                sorted_right -= 1
            elif item <= lc:
                A[i] = A[sorted_left+1]
                INSLEFT(A, item, sorted_left, 0)
                sorted_left += 1
                i += 1
            else:
                i += 1
        
        sorted_left += 1
        sorted_right -= 1

def counting_sort(A = [], B = [], k = 0):
    # Make Counting-Sort Algorithm Here
    # A = Main Array
    # B = Return Array
    # k = Biggest Value in A
    n = len(A)
    pass

def generate_dataset(n = 1):
    # Make Generate-Dataset Algorithm Here
    dataset = [0]*n
    for i in range(0,n-1):
        dataset[i] = random.randint(0,n)
    return dataset

A = generate_dataset(10)
print(A)
bidirectional_conditional_insertion_sort(A)
print(A)