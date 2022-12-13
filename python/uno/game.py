import uno.unocard as card_class
import uno.player as player_class


class Game:
    players = []
    player_turn = 0
    on_table = card_class.UnoCards.Empty
    game_ended = False
    last_action = "Game started"

    turn_number = 0

    def add_player(self, name):
        if len(name) <= 1:
            return "Enter longer name"
        if len(name) > 24:
            return "Enter shorter name"
        for c in self.players:
            if c.name == name:
                return "Player already exists"
        self.players.append(player_class.Player(name))
        return ""

    def add_cards(self, amount):
        for player in self.players:
            player.add_cards(amount)

    def has_ended(self):
        return False
