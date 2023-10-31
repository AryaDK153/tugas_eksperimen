from bcis import bidirectional_conditional_insertion_sort as do_bcsi
from generate_dataset import generate_dataset
from counting_sort import counting_sort as do_cs

'''ONLY FOR TESTING WHETHER THE CODES WORK'''

A = generate_dataset(10)
print("Original Order:", A)
B = A.copy()
C = A.copy()
print("# Sorting with BCIS #")
do_bcsi(B)
print(B)
print("# Sorting with Counting-Sort #")
do_cs(C)
print(C)