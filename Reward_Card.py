import itertools
class Reward_Card:
    CHARACTER = ['трансформер', 'кошка', 'редиска', 'суши', 'герл','джокер']
    CHARACTER_LETTERS = {'т': 'трансформер', 'г': 'герл', 'к': 'кошка', 'с': 'суши', 'р': 'редиска', 'д': 'джокер'}
    POINTS = [3, 5, 7, 12]
    COUNT = [2,3,4]

    def __init__(self, character: list, points):
        for i in character:
            if i in self.CHARACTER:
                self.character = character  # 'red' vs 'r'
            else:
                raise ValueError(f'Wrong character {character}')

        if 3 <= points <= 12:
            self.points = points
        else:
            raise ValueError(f'Wrong points {points}')

    def __repr__(self):
        text_c = ''
        for i in self.character:
            text_c += i[0]

        return f'{text_c}{self.points}'

    def __eq__(self, other):
        return self.character == other.character and self.points == other.points

    def __hash__(self):
        return hash((tuple(self.character), self.points))

    @staticmethod
    def create(text: str):
        """ По тексту вида 'тг3' возвращается карта Card('трансформергерл', 3)."""
        letter = []
        if text[-2] == '1':
            points = int(text[-2]+text[-1])
            for i in range(len(text) - 2):
                letter.append(Reward_Card.CHARACTER_LETTERS.get(text[i], None))
        else:
            points = int(text[-1])
            for i in range(len(text) - 1):
                letter.append(Reward_Card.CHARACTER_LETTERS.get(text[i], None))
        return Reward_Card(letter, points)

    @staticmethod
    def card_list(text: str):
        """ Из строки вида 'тг3 тт5 тдд12' возвращает список соответствующих карт."""
        return [Reward_Card.create(word) for word in text.split()]

    @staticmethod
    def all_cards():
        """ Выводит все возможные комбинации карт составленных из 2, 3 и 4 персонажей и цифры. """
        combinations = set()  # Множество для хранения уникальных комбинаций
        for count in Reward_Card.COUNT:
            for chars in itertools.permutations(Reward_Card.CHARACTER, count):
                for points in Reward_Card.POINTS:
                    combination = Reward_Card(list(chars), points)
                    combinations.add(combination)
        return combinations
print(Reward_Card.all_cards())
