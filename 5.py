while True:
    n = int(input("Enter a number between 1 and 9: "))
    if 0 < n < 10:
        break

print()

i = 1
while i <= n:
     print(' ' * (n - i), end='')


    j = i
    while j > 1:
        print(j, end=' ')
        j -= 1


    k = 1
    while k <= i:
        print(k, end=' ')
        k += 1

    print()
    i += 1
