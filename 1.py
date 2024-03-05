import random

num_players = int(input("შეიყვანეთ მოთამაშეების რაოდენობა: "))

if num_players > 0:
    for player in range(1, num_players + 1):
        gamer1 = random.randint(1, 6)
        gamer2 = random.randint(1, 6)
        print(f" {player}: {gamer1} {gamer2}")
else:
    print("გთხოვთ, შეიყვანეთ სწორი მოთამაშეების რაოდენობა (0-ზე მეტი).")
