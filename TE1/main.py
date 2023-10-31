from bcis import bidirectional_conditional_insertion_sort as do_bcsi
from generate_dataset import generate_dataset_arraymode
from counting_sort import counting_sort as do_cs

'''ONLY FOR TESTING WHETHER THE CODES WORK'''

data_source = input("press 1 for dataset.txt | press 2 for generate new")
if data_source == "1":
    datas = open("dataset.txt", "r")
    print(len(datas))
    print(datas.readline())
while True:
    try:
        A = generate_dataset_arraymode(int(input("Insert Dataset Length: ")))
        break
    except:
        print("Wrong input type! Try Again")
print("Original Order:", A)
B = A.copy()
C = A.copy()
print("# Sorting with BCIS #")
do_bcsi(B)
print(B)
print("# Sorting with Counting-Sort #")
do_cs(C)
print(C)