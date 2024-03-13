print()


while True:
    n = int(input("Enter a number between 1 and 9: "))
    if 0 < n < 10:
        break


print()


i = 1
while i < (n * 2):
    j = 1
    while j <= abs(n - i) + 1:
        print(j, end=" ")
        j += 1
    print()
    i += 1
