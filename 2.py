import random
import math

values = [10, 100, 100000, 10000000]

for n in values:
    counter = 0
    for _ in range(n):
        a = random.random()
        b = random.random()
        if math.sqrt(a ** 2 + b ** 2) <= 1:
            counter += 1
    print("output")
