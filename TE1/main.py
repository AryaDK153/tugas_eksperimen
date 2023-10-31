from time import sleep
from bcis import bidirectional_conditional_insertion_sort as do_bcsi
from generate_dataset import generate_dataset_arraymode
from counting_sort import counting_sort as do_cs

'''ONLY FOR TESTING WHETHER THE CODES WORK'''

while True:
    data_source = input("press 1 for dataset.txt | press 2 for generate new\nAnswer: ")
    if data_source == "1":
        datas = open("TE1\dataset.txt", "r")
        i = int(input("1 for Small (500 data) | 2 for Medium (5000 data) | 3 for Big (50000 data)\nAnswer: "))
        if i == 1:
            size = "Small"
        elif i == 2:
            size = "Medium"
            datas.readline()
        elif i == 3:
            size = "Big"
            datas.readline()
            datas.readline()
        print(f"========================== Dataset #{i}: {size} ==========================")
        data = datas.readline().split(" ")
        A = []
        for e in data:
            try:
                A.append(int(e))
            except:
                break
        print("Original Order:", A)
        B = A.copy()
        C = A.copy()


        print("# Sorting with BCIS #")
        do_bcsi(B)
        print(B)
        
        
        # print("# Sorting with Counting-Sort #")
        # do_cs(C)
        # print(C)
        
        datas.close()
        break
    elif data_source == "2":
        while True:
            try:
                A = generate_dataset_arraymode(int(input("Insert Dataset Length: ")))
                print("Original Order:", A)
                B = A.copy()
                C = A.copy()
                print("# Sorting with BCIS #")
                do_bcsi(B)
                print(B)
                print("# Sorting with Counting-Sort #")
                do_cs(C)
                print(C)
                break
            except:
                print("Wrong input type! Please Try Again\n\n")
        break
    print("Unknown Input! Please Try Again\n\n")
