
import random


computer_number = random.randint(0, 100)

user_number = int(input("შეიყვანეთ რიცხვი 0-დან 100-მდე: "))

if user_number == computer_number:
    print("You are winner.")
elif user_number > computer_number:
    print("high.")
else:
    print("low.")


for _ in range(9):

    user_number = int(input("შეიყვანეთ რიცხვი 0-დან 100-მდე: "))


    if user_number == computer_number:
        print("You are winner.")
        break
    elif user_number > computer_number:
        print("high.")
    else:
        print("low.")


print("Computer is winner.")
