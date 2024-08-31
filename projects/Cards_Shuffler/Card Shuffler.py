import random

def generate_deck():
    values = [str(i) for i in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']
    suits = ['spades', 'clubs', 'diamonds', 'hearts']
    deck = []

    for suit in suits:
        for value in values:
            deck.append({'value': value, 'suit': suit})

    return deck

def shuffle_deck(deck):
    random.shuffle(deck)

def display_deck(deck):
    for card in deck:
        if card['suit'] in ['diamonds', 'hearts']:
            print(f"\033[31m{card['value']} {card['suit']}\033[0m")  # red text
        else:
            print(f"\033[97m{card['value']} {card['suit']}\033[0m")  # white text

if __name__ == "__main__":
    deck = generate_deck()
    shuffle_deck(deck)
    display_deck(deck)
