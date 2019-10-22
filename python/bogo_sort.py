import random

def is_sorted(data):
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True

def bogosort(data):
    while not is_sorted(data):
        random.shuffle(data)
    return data
