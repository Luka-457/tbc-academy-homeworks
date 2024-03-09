
n = int(input("Enter a natural number (0 < n < 50): "))


if 0 < n < 50:
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(f"{spaces}{stars}{spaces}")

    tree = " " * (n - 1)
    print(f"{tree}|{tree}")
    print(f"{tree}|{tree}")
else:
    print("Please enter a valid natural number ")

