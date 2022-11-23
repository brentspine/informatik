import uno.unocard as card_class


class Player:
    name = "Player"
    hand = []

    def __init__(self, name, hand=[]):
        self.name = name
        self.hand = hand

    def add_cards(self, amount):
        for i in range(amount):
            self.hand.append(card_class.generate_random())

