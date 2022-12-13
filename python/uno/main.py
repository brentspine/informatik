import random
import os

import uno.unocard as card_class
import uno.game as game_class
import uno.player as player_class


clear = "\n" * 100

def main():
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
        game.add_cards(1)
        names = []
        list(map(lambda c: c.add_name_to_list(names), game.players))
        print("Players: " + str(names))
        while not game.has_ended():
            for player in game.players:
                print(clear)
                print("Pass to " + player.name)
                input("\n" * 7)
                print(clear)
                print("Your hand: " + player.get_hand_string())
                # print("Playable options: " + player.get_play_string())
                print(" ")
                input("Enter card to play: ")

                if game.has_ended(): break


if __name__ == "__main__":
    main()

