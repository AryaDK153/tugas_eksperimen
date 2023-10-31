import random

def generate_dataset_arraymode(n = 1):
    # Make Generate-Dataset Algorithm Here
    dataset = [0]*n
    for i in range(0,n-1):
        dataset[i] = random.randint(0,n)
    return dataset