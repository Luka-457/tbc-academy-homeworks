string1 = input("Input: ").strip().replace(" ", "").lower()
string2 = input().strip().replace(" ", "").lower()

found_chars = []

for char in string2:
    if char in string1:
        found_chars.append(True)
    else:
        found_chars.append(False)
        break

if all(found_chars):
    print("Output: YES")
else:
    print("Output: NO")




