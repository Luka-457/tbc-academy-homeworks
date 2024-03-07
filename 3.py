side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))
perimeter = side1 + side2 + side3
semi_perimeter = perimeter / 2
area = (semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))**0.5
print("The perimeter of the triangle is:", perimeter)
print("The area of the triangle is:", area)
