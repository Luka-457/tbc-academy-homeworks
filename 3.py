
input_speed = int(input("Enter your car speed in KM/h: "))


if input_speed < 30:
    print("SLOW")
elif input_speed > 120:
    print("VERY FAST")
elif input_speed > 60:
    print("FAST")
elif input_speed > 30:
    print("MODERATE")
