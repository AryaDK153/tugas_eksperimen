import random

def generate_dataset_arraymode(n = 1):
    if n < 1:
        return []
    # Make Generate-Dataset Algorithm Here
    # For generating new while running a caller program
    dataset_sorted = [0]*n
    last_k = 0
    for i in range(0,n-1):
        last_k = random.randint(last_k, last_k+5)
        dataset_sorted[i] = last_k
    
    dataset_random = [0]*n
    for i in range(0,n-1):
        dataset_random[i] = random.randint(0, n+1)

    dataset_reverse = [0]*n
    last_k = n*2
    for i in range(0,n-1):
        last_k = random.randint(last_k-3, last_k)
        if last_k <= 0:
            last_k = 0
        dataset_reverse[i] = last_k
    
    return dataset_sorted, dataset_random, dataset_reverse

def generate_dataset_txtmode(n = 1):
    if n < 1:
        return []
    # Make Generate-Dataset Algorithm Here
    # For inserting into dataset.txt
    dataset = ""
    last_k = 0
    for i in range(0,n-1):
        last_k = random.randint(last_k, last_k+5)
        dataset += f"{last_k} "
    dataset += "\n"

    for i in range(0,n-1):
        dataset += f"{random.randint(0, n+1)} "
    dataset += "\n"

    last_k = n*2
    for i in range(0,n-1):
        last_k = random.randint(last_k-3, last_k)
        if last_k <= 0:
            last_k = 0
        dataset += f"{last_k} "
    dataset += "\n"
    return dataset

# Run IF AND ONLY IF you want to get new datasets in dataset.txt
if __name__ == "__main__":
    file = open("TE1\dataset.txt", "w")
    to_write = ""
    size = 500
    for i in range(3):
        to_write += f"{generate_dataset_txtmode(size)}\n"
        size *= 10
    file.write(to_write)
    file.close()
    print("Created new datasets for dataset.txt")