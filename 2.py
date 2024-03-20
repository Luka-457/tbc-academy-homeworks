word = input("Enter a word: ")

consonants = ""

for letter in word:
    if letter.lower() not in 'aeiou':
        consonants += letter

print("Consonant letters:", consonants)



