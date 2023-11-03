from bcis import bidirectional_conditional_insertion_sort as do_bcis
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
            for i in range(4):
                datas.readline()
        elif i == 3:
            size = "Big"
            for i in range(7):
                datas.readline
        print(f"========================== Dataset #{i}: {size} ==========================")
        for i in range(3):
            data = datas.readline().split(" ")
            A = []
            for e in data:
                try:
                    A.append(int(e))
                except:
                    break
            if i == 0:
                sorted_set = A
            elif i == 1:
                random_set = A
            elif i == 2:
                reverse_set = A
        print(f"Original Order:\n# Sorted #\n{sorted_set}\n# Random #\n{random_set}\n# Reverse #\n{reverse_set}")

        while True:
            method = input("1 for BCIS | 2 for Counting-Sort\nAnswer: ")
            if method == "1":
                print("\n# Sorting with BCIS #")
                do_bcis(sorted_set)
                print(f"# From Sorted #\n{sorted_set}")
                do_bcis(random_set)
                print(f"# From Random #\n{random_set}")
                do_bcis(reverse_set)
                print(f"# From Reverse #\n{reverse_set}")
                break
            elif method == "2":
                print("\n# Sorting with Counting-Sort #")
                do_cs(sorted_set)
                print(f"# From Sorted #\n{sorted_set}")
                do_cs(random_set)
                print(f"# From Random #\n{random_set}")
                do_cs(reverse_set)
                print(f"# From Reverse #\n{reverse_set}")
                break
            else:
                print("Wrong input! Please Try Again\n\n")
        break
        
        datas.close()
        break
    elif data_source == "2":
        while True:
            try:
                sorted_set, random_set, reverse_set = generate_dataset_arraymode(int(input("Insert Dataset Length: ")))
                print(f"Original Order:\n# Sorted #\n{sorted_set}\n# Random #\n{random_set}\n# Reverse #\n{reverse_set}")
                break
            except:
                print("Wrong input type! Please Try Again\n\n")
        
        while True:
            method = input("1 for BCIS | 2 for Counting-Sort\nAnswer: ")
            if method == "1":
                print("\n# Sorting with BCIS #")
                do_bcis(sorted_set)
                print(f"# From Sorted #\n{sorted_set}")
                do_bcis(random_set)
                print(f"# From Random #\n{random_set}")
                do_bcis(reverse_set)
                print(f"# From Reverse #\n{reverse_set}")
                break
            elif method == "2":
                print("\n# Sorting with Counting-Sort #")
                do_cs(sorted_set)
                print(f"# From Sorted #\n{sorted_set}")
                do_cs(random_set)
                print(f"# From Random #\n{random_set}")
                do_cs(reverse_set)
                print(f"# From Reverse #\n{reverse_set}")
                break
            else:
                print("Wrong input! Please Try Again\n\n")
        break
    print("Unknown Input! Please Try Again\n\n")
