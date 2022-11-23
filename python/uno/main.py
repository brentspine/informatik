import random

import uno.unocard as card_class
import uno.game as game_class
import uno.player as player_class


def main():s
    while True:
        game = game_class.Game()
        while True:
            name = input("Enter player " + str(len(game.players) + 1) + ": ")
            if name == "end":
                if len(game.players) <= 1:
                    print("Not enough players")
                    continue
                else:
                    break
            r = game.add_player(name)
            if len(r) > 0:
                print(r)
            else:
                print("Added player " + name)



if __name__ == "__main__":
    main()
