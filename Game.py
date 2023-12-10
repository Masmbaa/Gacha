import pygame
import random

pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Гача")

icon = pygame.image.load("Иконка.png")
pygame.display.set_icon(icon)

# class Hand:
#     def __init__(self, x, y, width, height, ):
main_color = (238, 190, 241)

card_width = 100
card_height = 150

clock = pygame.time.Clock()


def Character_Deck():
    """Создает список всей колоды с гаяа картами"""
    С_deck = []
    elements = ['т', 'ф', 'к', 'с', 'р']

    for element in elements:
        С_deck.extend([element] * 15)

    return С_deck


C_deck = Character_Deck()


def hand_card(C_deck):
    """Выбирает 4 карты для руки и удаляет из колоды эти карты"""
    card1 = []
    if len(C_deck) > 0:
        for i in range(4):
            card1.append(random.choice(C_deck))
            C_deck.remove(card1[i])
        return card1
    else:
        return None


hand_card = hand_card(C_deck)


def size_hand():
    """Задает х и у карт"""
    card_x = []
    for i in range(4):
        card_x.append(display_width / 2 - card_width * 2 + i * card_width)
    card_y = display_height - card_height - 50
    return card_x, card_y


def Card_images():
    """Формирует изображения карт в руке"""
    hand_card_images = []
    for i in range(4):
        hand_card_images.append(pygame.image.load(f"{hand_card[i]}.jpg"))
        hand_card_images[i] = pygame.transform.scale(hand_card_images[i], (card_width, card_height))
    return hand_card_images

# def Reward_cards():

def ran_game():
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.fill(main_color)

        card_x, card_y = size_hand()
        hand_card_images = Card_images()

        for x in range(4):
            display.blit(hand_card_images[x], (card_x[x] + x * 5, card_y, card_width, card_height))

        pygame.display.update()
        clock.tick(60)


ran_game()