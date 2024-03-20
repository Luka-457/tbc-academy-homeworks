user_input = input("Please enter a word or phrase: ")
for i in range(0, len(user_input), 2):
    if user_input[i] != 'e':
        print(user_input[i], end='')
