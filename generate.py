#from random import choice
import random
#coin=random.choice(["heads", "tails"])
coin=random.choice(["grace","millena"])
print(coin)
number=random.randint(1,9)
print(number)
cards=["jack","king","queen","hearts"]
random.shuffle(cards)
for card in cards:
    print(card)

