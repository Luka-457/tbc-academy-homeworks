keyboard = "qwertyuiopasdfghjklzxcvbnm"
action = input("Enter action (e/d): ").lower()
while action not in ['e', 'd']:
    action = input("Invalid input! Please enter 'e' for encryption or 'd' for decryption: ").lower()

text = input("Enter text: ")

shifted_chars = {}
for i in range(len(keyboard)):
    if action == 'e':
        shifted_chars[keyboard[i]] = keyboard[(i + 1) % len(keyboard)]
    elif action == 'd':
        shifted_chars[keyboard[i]] = keyboard[(i - 1) % len(keyboard)]

result = ""

for char in text:
    if char.islower() and char.isalpha():
        result += shifted_chars[char]
    else:
        result += char

print("Result:", result)
