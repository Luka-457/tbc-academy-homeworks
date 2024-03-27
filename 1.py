values = [10, 100, 10000, 100000]

for n in values:
    x = 0
    sign = 1
    for i in range(1, n + 1):
        x += sign * 1 / (2 * i - 1)
        sign *= -1
    x *= 4
    print("output")
