PASSWORD = "BATMAN"


print("Welcome to the Secure Zone!\n")


user_name = input("What's your name? ")


for attempt in range(3):
    entered_password = input("Please enter your password: ")


    if entered_password == PASSWORD:
        print("Welcome back, " + user_name + "!")
        break
    else:
        if attempt == 2:
            print("Too many incorrect attempts. Temporary block. Try again later.")
        else:
            print("Invalid password. Please try again.")


print("\nThank you for using our system.")



    





