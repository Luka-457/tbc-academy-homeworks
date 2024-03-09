
for i in range(1, 10):
    row_values = []
    for j in range(1, 10):
        number = i * j
        if number not in row_values:
            row_values.append(number)
            print(f"{i} * {j} = {number}", end="  ")
    print()


    





