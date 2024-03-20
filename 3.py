word = input("Enter a word: ")

length = len(word)
middle = length // 2

while_count = 5
while while_count > 0:
    if length % 2 == 0:
        print("Middle two letters:", word[middle - 1:middle + 1])
    else:
        print("First letter:", word[0])
        print("Middle letter:", word[middle])
        print("Last letter:", word[-1])
    while_count -= 1

