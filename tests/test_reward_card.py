import pytest
from Reward_Card import Reward_Card

class TestRewardCard:
    def test_init_valid(self):
        card = Reward_Card(['трансформер', 'герл'], 3)
        assert card.character == ['трансформер', 'герл']
        assert card.points == 3

    def test_init_invalid_character(self):
        with pytest.raises(ValueError):
            Reward_Card(['invalid', 'герл'], 3)

    def test_init_invalid_points(self):
        with pytest.raises(ValueError):
            Reward_Card(['трансформер', 'герл'], 15)

    def test_repr(self):
        card = Reward_Card(['трансформер', 'герл'], 3)
        assert repr(card) == 'тг3'

    def test_eq(self):
        card1 = Reward_Card(['трансформер', 'герл'], 3)
        card2 = Reward_Card(['трансформер', 'герл'], 3)
        card3 = Reward_Card(['трансформер'], 3)
        assert card1 == card2
        assert card1 != card3

    def test_create(self):
        card = Reward_Card.create('тг3')
        assert card.character == ['трансформер', 'герл']
        assert card.points == 3

    def test_card_list(self):
        cards = Reward_Card.card_list('тг3 тт5 тдд12')
        assert len(cards) == 3
        assert cards[0].character == ['трансформер', 'герл']
        assert cards[0].points == 3
        assert cards[1].character == ['трансформер', 'трансформер']
        assert cards[1].points == 5
        assert cards[2].character == ['трансформер', 'джокер', 'джокер']
        assert cards[2].points == 12

    def test_all_cards(self):
        combinations = Reward_Card.all_cards()
        assert len(combinations) == 2040
