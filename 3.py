
n = int(input("Enter a number between 0 and 9999: "))

while not (0 <= n < 10000):
    n = int(input( "That's not a valid number. Please enter a number between 0 and 9999: "))

reversed_fraction = 1 / n

sum_of_digits = 0
reversed_number = 0

while n > 0:
    last_digit = n % 10
    sum_of_digits += last_digit
    reversed_number = (reversed_number * 10) + last_digit
    n //= 10

print("Reversed number is:", reversed_number)
print("Sum of digits:", sum_of_digits)
print("Reversed fraction of the entered number is:", reversed_fraction)
