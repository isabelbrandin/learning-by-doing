import random

def randomlist(a):
    rali = []
    for i in range(a):
        rali.append(random.randint(0, 100))
    return rali

print(randomlist(10))