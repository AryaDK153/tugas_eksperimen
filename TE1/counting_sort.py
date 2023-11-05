'''
Referenced from the Pseudocode from:
CLRS. (2009). Ch. 8.2 Counting-Sort. Introduction to Algorithms. London: The MIT Press.
'''
def find_biggest(A = []):
    # A method for finding the biggest (highest) value in array A
    result = A[0]
    for e in A:
        if result < e:
            result = e
    return result

def counting_sort(A = []):
    # Make Counting-Sort Algorithm Here
    # A = Main Array
    # B = Temp Array
    # k = Biggest Value in A
    n = len(A)
    if n < 1:
        return
    B = A.copy()
    for i in range(0, n):
        A[i] = 0

    k = find_biggest(B)
    C = [0] * (k+1)
    for j in range(0, n):
        C[B[j]] += 1
    # print(f"A{A}\nB{B}\nC{C}")

    for i in range(1, k+1):
        C[i] += C[i-1]
    # print(f"A{A}\nB{B}\nC{C}")
    
    for j in range(n-1, -1, -1):
        A[C[B[j]]-1] = B[j]
        C[B[j]] -= 1