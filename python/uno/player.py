import uno.unocard as card_class


class Player:
    name = "Player"
    hand = []

    def __init__(self, name, hand=[]):
        self.name = name
        self.hand = hand

    def add_cards(self, amount):
        for i in range(amount):
            print(card_class.generate_random().display)
            self.hand.append(card_class.generate_random())

    def add_name_to_list(self, list):
        list.append(self.name)

    def get_hand_string(self):
        r = ""
        for c in self.hand:
            r += c.display + ", "
        return r

    def get_play_string(self):
        r = ""
        a = []
        for c in self.hand:
            if c.name in a: continue
            r += c.name + ", "
            a.append(c.name)
        return r
