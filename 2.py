import random


n = int(input("Enter a number (0 < n < 30): "))


if 0 < n < 30:

    numbers = [random.randint(0, 1000) for _ in range(n)]


    print(f"Random numbers: {numbers}")


    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num


    print(f"The maximum number is: {max_number}")
else:
    print("Please enter a valid number (0 < n < 30).")
