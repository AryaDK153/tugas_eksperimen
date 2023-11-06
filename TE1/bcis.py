from math import floor, ceil, sqrt

'''
Referenced from the Pseudocode from:
Adnan Saher Mohammed, S¸ahin Emrah Amrahov, and Fatih V C¸ elebi. Bidirectional Conditional
    Insertion Sort algorithm; An efficient progress on the classical insertion sort. Future Generation
    Computer Systems, 71:102–112, 2017.

In this implementation, I've made sure to adjust codes to make sure the indexing starts from 0 to (n-1),
where 0 as the left-most index of the dataset and (n-1) as the right-most index.
'''

def bidirectional_conditional_insertion_sort(A = []):
    # Make Bidirectional-Conditional-Insertion-Sort Algorithm Here
    # A = Main Array

    'BCIS Functions'
    def SWAP(A = [], i = 0, j = 0):
        A[i], A[j] = A[j], A[i]
    def ISEQUAL(A = [], sl = 0, sr = 0):
        for k in range(sl+1, sr):
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
        if A[sorted_right] < A[sorted_left]:
            SWAP(A, sorted_right, sorted_left+(int(ceil((sorted_right-sorted_left)/2))))
        # print("\nUncon-swap\n", A)
        if A[sorted_left] == A[sorted_right]:
            if ISEQUAL(A, sorted_left, sorted_right) == -1:
                return
        # print("\nfirstifswap\n", A)
        if A[sorted_left] > A[sorted_right]:
            SWAP(A, sorted_left, sorted_right)
        # print("\nsecondifswap", A)
        if (sorted_right-sorted_left) >= 100:
            for i in range(sorted_left+1, floor(sqrt(sorted_right-sorted_left)+1)):
                if A[sorted_right] < A[i]:
                    SWAP(A, sorted_right, i)
                elif A[sorted_left] > A[i]:
                    SWAP(A, sorted_left, i)
        else:
            i = sorted_left+1
        
        # print(A)
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
        # print(A)
        # input("<<Enter>>")