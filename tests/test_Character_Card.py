import pytest
from Character_Card import Character_Card

def test_create_character_card():
    card = Character_Card.create('т')
    assert card.character == 'трансформер'

def test_create_character_card_invalid():
    with pytest.raises(ValueError):
        Character_Card.create('a')

def test_card_list():
    cards = Character_Card.card_list('т к р с')
    assert len(cards) == 4
    assert cards[0].character == 'трансформер'
    assert cards[1].character == 'кошка'
    assert cards[2].character == 'редиска'
    assert cards[3].character == 'суши'

def test_all_cards():
    cards = Character_Card.all_cards()
    assert len(cards) == 5
    assert cards[0].character == 'трансформер'
    assert cards[1].character == 'кошка'
    assert cards[2].character == 'редиска'
    assert cards[3].character == 'суши'
    assert cards[4].character == 'герл'
