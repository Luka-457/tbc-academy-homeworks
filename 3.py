import random


suits = ["♣", "♦", "♥", "♠"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


random_card = random.choice(values) + random.choice(suits)


print("Your card is:", random_card)
