import pytest

class Character_Card:
    CHARACTER = ['трансформер', 'кошка', 'редиска', 'суши', 'герл']
    CHARACTER_LETTERS = {'т': 'трансформер', 'г': 'герл', 'к': 'кошка', 'с': 'суши', 'р': 'редиска'}


    def __init__(self, character):
        if character in self.CHARACTER:
            self.character = character  # 'red' vs 'r'
        else:
            raise ValueError(f'Wrong character {character}')


    def __repr__(self):
        return f'{self.character[0]}'

    def __eq__(self, other):
        return self.character == other.character

    @staticmethod
    def create(text: str):
        """ По тексту вида 'т' возвращается карта Character_Card('трансформер')."""
        letter = Character_Card.CHARACTER_LETTERS.get(text[0], None)
        return Character_Card(letter)

    @staticmethod
    def card_list(text: str):
        """ Из строки вида 'т к р с' возвращает список соответствующих карт."""
        return [Character_Card.create(word) for word in text.split()]

    @staticmethod
    def all_cards():
        """ Все карты для создания колоды. """
        return [Character_Card(character) for character in Character_Card.CHARACTER]

print(repr(Character_Card.all_cards()))