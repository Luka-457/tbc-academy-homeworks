n = int(input("Enter a positive integer (0 < n <= 1000): "))

if 0 < n <= 1000:
    print(n, end=" -> ")

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1

        print(n, end=" -> ")
else:
    print("Invalid input. Please enter a number between 1 and 1000.")


