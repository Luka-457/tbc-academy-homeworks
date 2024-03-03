# Get user input for a number
number = int(input("შეიყვანეთ რიცხვი: "))

# Check for prime numbers and divisors
if number == 2 or number == 7:
    print(f"{number} არის პირველი რიცხვი.")
elif number == 4 or number == 8:
    print(f"{number} იყოფა 2-ზე. 2 არის პირველი რიცხვი.")
elif number == 6:
    print(f"{number} იყოფა 2-ზე და 3-ზე. 2 და 3 არიან პირველი რიცხვები.")
elif number == 9:
    print(f"{number} იყოფა 3-ზე. 3 არის პირველი რიცხვი.")
elif number == 5:
    print(f"{number} არის პირველი რიცხვი.")
elif number == 10:
    print(f"{number} იყოფა 2-ზე და 5-ზე. 2 და 5 არიან პირველი რიცხვები.")
else:
    print("შეცდომა. გთხოვთ შეიყვანოთ რიცხვი 2-დან 10-მდე.")
