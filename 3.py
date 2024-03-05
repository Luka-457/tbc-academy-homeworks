number = int(input("Enter a positive whole number (0 < n < 1000): "))

if 0 < number < 1000:
    divisors = []

    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)

    print(f"The divisors of {number} are: {divisors}")
else:
    print("Please enter a valid number within the specified range.")
