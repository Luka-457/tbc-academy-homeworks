text = input("Input: ")

filtered_text = ''.join(char.lower() for char in text if 'a' <= char <= 'z' or 'A' <= char <= 'Z')

is_palindrome = filtered_text == filtered_text[::-1]

if is_palindrome:
    print("Output: Is palindrome")
else:
    print("Output: Is not palindrome")

