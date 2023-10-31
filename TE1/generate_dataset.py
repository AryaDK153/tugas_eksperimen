import random

def generate_dataset_arraymode(n = 1):
    # Make Generate-Dataset Algorithm Here
    # For generating new while running a caller program
    dataset = [0]*n
    for i in range(0,n-1):
        dataset[i] = random.randint(0,n+1)
    return dataset

def generate_dataset_txtmode(n = 1):
    # Make Generate-Dataset Algorithm Here
    # For inserting into dataset.txt
    dataset = ""
    for i in range(0,n-1):
        dataset += f"{random.randint(0,n+1)} "
    return dataset

# Run IF AND ONLY IF you want to get new datasets in dataset.txt
file = open("TE1\dataset.txt", "w")
to_write = ""
size = 500
for i in range(3):
    to_write += f"{generate_dataset_txtmode(size)}\n"
    size *= 10
file.write(to_write)
file.close()