while True:
    n = int(input("Please enter a non-negative integer (0 <= n < 20): "))
    if 0 <= n < 20:
        break

number_1 = 0
number_2 = 1

if n == 0:
    print(number_1)

elif n == 1:
    print(number_1, number_2)

else:
    print(number_1, number_2, end=" ")


    while n > 1:
        next_number = number_1 + number_2
        print(next_number, end=" ")

        number_1, number_2 = number_2, next_number

         n -= 1
