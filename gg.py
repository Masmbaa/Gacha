import random


def create_deck():
    deck = []
    elements = ['т', 'г', 'к', 'с', 'р']

    for element in elements:
        deck.extend([element] * 15)

    return deck


def draw_card(deck):
    card1 = []
    if len(deck) > 0:
        for i in range(4):
            card1.append(random.choice(deck))
            card = card1[i]
            deck.remove(card)
        return card1
    else:
        return None


deck = create_deck()
print("Колода карт:", deck)

card = draw_card(deck)
if card:
    print("Извлеченные карты:", card)
    print("Обновленная колода карт:", deck)
else:
    print("Колода пуста!")