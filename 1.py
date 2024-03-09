input_num = input("Enter a natural number up to and including 50: ")

if input_num.isdigit():
    number = int(input_num)
    if 0 < number <= 50:
        for num in range(1, number + 1):
            divisors = [i for i in range(1, num + 1) if num % i == 0]
            print(f"{num} - {divisors[:3]}")
    elif number == 0:
        print("Zero cannot be divided")
    else:
        print("Please enter a natural number up to and including 50")
else:
    print("Please enter only numbers.")

